#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube Audio Downloader - Web Server
Servidor Flask para download de áudio do YouTube
"""

from flask import Flask, request, jsonify, send_file, render_template
import os
import subprocess
import tempfile
import shutil
from pathlib import Path
import uuid
import threading
import time

app = Flask(__name__, static_folder='.')

# Pasta para downloads temporários
DOWNLOAD_FOLDER = tempfile.mkdtemp()
# Limpeza automática de arquivos antigos (mais de 1 hora)
CLEANUP_INTERVAL = 3600

def cleanup_old_files():
    """Remove arquivos com mais de 1 hora"""
    while True:
        try:
            current_time = time.time()
            for filename in os.listdir(DOWNLOAD_FOLDER):
                filepath = os.path.join(DOWNLOAD_FOLDER, filename)
                if os.path.isfile(filepath):
                    if current_time - os.path.getctime(filepath) > 3600:
                        os.remove(filepath)
                        print(f"Arquivo removido: {filename}")
        except Exception as e:
            print(f"Erro na limpeza: {e}")
        time.sleep(CLEANUP_INTERVAL)

# Iniciar thread de limpeza
cleanup_thread = threading.Thread(target=cleanup_old_files, daemon=True)
cleanup_thread.start()

@app.route('/')
def index():
    """Serve a página inicial"""
    return send_file('index.html')

@app.route('/download', methods=['POST'])
def download():
    """Endpoint para download de áudio"""
    try:
        print("=" * 50)
        print("Nova requisição de download recebida")

        data = request.get_json()
        print(f"Dados recebidos: {data}")

        url = data.get('url', '').strip()
        audio_format = data.get('format', 'mp3')

        print(f"URL: {url}")
        print(f"Formato: {audio_format}")

        # Validação
        if not url:
            print("Erro: URL não fornecida")
            return jsonify({'error': 'URL não fornecida'}), 400

        if not url.startswith(('http://', 'https://')):
            print("Erro: URL inválida")
            return jsonify({'error': 'URL inválida'}), 400

        # Gerar nome único para o arquivo
        file_id = str(uuid.uuid4())
        print(f"ID do arquivo: {file_id}")

        # Configurar template de saída
        output_template = os.path.join(DOWNLOAD_FOLDER, f"{file_id}.%(ext)s")

        print(f"Iniciando download: {url} em formato {audio_format}")

        # Comando yt-dlp
        if audio_format == 'mp3':
            cmd = [
                'yt-dlp',
                '-x',
                '--audio-format', 'mp3',
                '--audio-quality', '0',  # Melhor qualidade
                '--embed-thumbnail',
                '--add-metadata',
                '-o', output_template,
                url
            ]
        else:  # wav
            cmd = [
                'yt-dlp',
                '-x',
                '--audio-format', 'wav',
                '-o', output_template,
                url
            ]

        # Executar download
        print(f"Executando comando: {' '.join(cmd)}")
        process = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300  # 5 minutos timeout
        )

        print(f"Código de retorno: {process.returncode}")

        if process.returncode != 0:
            error_msg = process.stderr if process.stderr else 'Erro desconhecido'
            print(f"Erro no download: {error_msg}")
            print(f"STDOUT: {process.stdout}")
            return jsonify({'error': 'Falha no download. Verifique a URL.'}), 500

        print("Download concluído com sucesso!")

        # Encontrar o arquivo baixado
        print(f"Procurando arquivo em: {DOWNLOAD_FOLDER}")
        print(f"Arquivos na pasta: {os.listdir(DOWNLOAD_FOLDER)}")

        downloaded_file = None
        for filename in os.listdir(DOWNLOAD_FOLDER):
            if filename.startswith(file_id):
                downloaded_file = filename
                print(f"Arquivo encontrado: {downloaded_file}")
                break

        if not downloaded_file:
            print("ERRO: Arquivo não encontrado após download")
            return jsonify({'error': 'Arquivo não encontrado após download'}), 500

        filepath = os.path.join(DOWNLOAD_FOLDER, downloaded_file)
        print(f"Caminho completo: {filepath}")

        # Retornar URL para download
        download_url = f'/get/{downloaded_file}'
        print(f"URL de download: {download_url}")
        print("=" * 50)

        return jsonify({
            'success': True,
            'download_url': download_url,
            'filename': downloaded_file
        })

    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Timeout: Download demorou muito tempo'}), 500
    except Exception as e:
        print(f"Erro: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/get/<filename>')
def get_file(filename):
    """Serve o arquivo para download"""
    try:
        filepath = os.path.join(DOWNLOAD_FOLDER, filename)

        if not os.path.exists(filepath):
            return jsonify({'error': 'Arquivo não encontrado'}), 404

        # Determinar nome amigável
        original_name = filename
        if '.' in filename:
            # Remove o UUID e mantém o nome original se possível
            parts = filename.split('.')
            extension = parts[-1]
            original_name = f"audio.{extension}"

        return send_file(
            filepath,
            as_attachment=True,
            download_name=original_name
        )
    except Exception as e:
        print(f"Erro ao servir arquivo: {str(e)}")
        return jsonify({'error': 'Erro ao baixar arquivo'}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'download_folder': DOWNLOAD_FOLDER})

if __name__ == '__main__':
    print("=" * 50)
    print("🎵 YouTube Audio Downloader Server")
    print("=" * 50)
    print(f"Pasta de downloads: {DOWNLOAD_FOLDER}")
    print("Servidor rodando em: http://127.0.0.1:5000")
    print("Pressione Ctrl+C para parar")
    print("=" * 50)

    # Verificar dependências
    try:
        subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        print("✓ yt-dlp encontrado")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ yt-dlp não encontrado! Instale com: pip install yt-dlp")

    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        print("✓ ffmpeg encontrado")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ ffmpeg não encontrado! Instale ffmpeg")

    print("=" * 50)

    app.run(debug=True, host='0.0.0.0', port=5000)
