#!/usr/bin/env python3
"""
YouTube Audio Downloader
Baixa áudio de vídeos do YouTube em MP3 ou WAV
AVISO: Use apenas para conteúdo que você tem direito de baixar!
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import sys
import threading
import subprocess

class YouTubeAudioDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Audio Downloader")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        
        # Variáveis
        self.download_path = tk.StringVar(value=os.path.expanduser("~/Downloads"))
        self.format_var = tk.StringVar(value="mp3")
        self.quality_var = tk.StringVar(value="best")
        self.url_var = tk.StringVar()
        
        self.setup_ui()
        self.check_dependencies()
    
    def setup_ui(self):
        # Título
        title_label = tk.Label(
            self.root, 
            text="🎵 YouTube Audio Downloader", 
            font=("Arial", 16, "bold"),
            pady=10
        )
        title_label.pack()
        
        # Aviso legal
        warning_frame = tk.Frame(self.root, bg="#fff3cd", bd=2, relief=tk.SOLID)
        warning_frame.pack(fill=tk.X, padx=20, pady=5)
        
        warning_label = tk.Label(
            warning_frame,
            text="⚠️ Use apenas para conteúdo que você tem direito de baixar!",
            bg="#fff3cd",
            fg="#856404",
            font=("Arial", 9)
        )
        warning_label.pack(pady=5)
        
        # Frame principal
        main_frame = tk.Frame(self.root, padx=20, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # URL do vídeo
        url_label = tk.Label(main_frame, text="URL do vídeo:", font=("Arial", 10, "bold"))
        url_label.pack(anchor=tk.W, pady=(5, 2))
        
        url_entry = tk.Entry(main_frame, textvariable=self.url_var, font=("Arial", 10))
        url_entry.pack(fill=tk.X, pady=(0, 10))
        
        # Formato
        format_frame = tk.Frame(main_frame)
        format_frame.pack(fill=tk.X, pady=5)
        
        format_label = tk.Label(format_frame, text="Formato:", font=("Arial", 10, "bold"))
        format_label.pack(side=tk.LEFT, padx=(0, 10))
        
        mp3_radio = tk.Radiobutton(
            format_frame, 
            text="MP3 (compacto)", 
            variable=self.format_var, 
            value="mp3"
        )
        mp3_radio.pack(side=tk.LEFT, padx=5)
        
        wav_radio = tk.Radiobutton(
            format_frame, 
            text="WAV (qualidade máxima)", 
            variable=self.format_var, 
            value="wav"
        )
        wav_radio.pack(side=tk.LEFT, padx=5)
        
        # Qualidade (apenas para MP3)
        quality_frame = tk.Frame(main_frame)
        quality_frame.pack(fill=tk.X, pady=5)
        
        quality_label = tk.Label(quality_frame, text="Qualidade MP3:", font=("Arial", 10, "bold"))
        quality_label.pack(side=tk.LEFT, padx=(0, 10))
        
        quality_combo = ttk.Combobox(
            quality_frame,
            textvariable=self.quality_var,
            values=["best", "320k", "256k", "192k", "128k"],
            state="readonly",
            width=10
        )
        quality_combo.pack(side=tk.LEFT)
        
        # Pasta de destino
        path_label = tk.Label(main_frame, text="Pasta de destino:", font=("Arial", 10, "bold"))
        path_label.pack(anchor=tk.W, pady=(10, 2))
        
        path_frame = tk.Frame(main_frame)
        path_frame.pack(fill=tk.X, pady=(0, 10))
        
        path_entry = tk.Entry(path_frame, textvariable=self.download_path, font=("Arial", 9))
        path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        browse_btn = tk.Button(
            path_frame, 
            text="Procurar...", 
            command=self.browse_folder,
            bg="#6c757d",
            fg="white",
            relief=tk.FLAT,
            padx=10
        )
        browse_btn.pack(side=tk.LEFT)
        
        # Barra de progresso
        self.progress_label = tk.Label(main_frame, text="", font=("Arial", 9))
        self.progress_label.pack(pady=(10, 2))
        
        self.progress_bar = ttk.Progressbar(
            main_frame, 
            mode='indeterminate', 
            length=400
        )
        self.progress_bar.pack(pady=(0, 10))
        
        # Botão de download
        self.download_btn = tk.Button(
            main_frame,
            text="⬇ Baixar Áudio",
            command=self.start_download,
            font=("Arial", 12, "bold"),
            bg="#28a745",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.download_btn.pack(pady=10)
        
        # Log
        log_label = tk.Label(main_frame, text="Log:", font=("Arial", 9, "bold"))
        log_label.pack(anchor=tk.W, pady=(5, 2))
        
        self.log_text = tk.Text(main_frame, height=6, font=("Courier", 8), bg="#f8f9fa")
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar para o log
        scrollbar = tk.Scrollbar(self.log_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.log_text.yview)
    
    def browse_folder(self):
        folder = filedialog.askdirectory(initialdir=self.download_path.get())
        if folder:
            self.download_path.set(folder)
    
    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def check_dependencies(self):
        """Verifica se yt-dlp e ffmpeg estão instalados"""
        try:
            subprocess.run(["yt-dlp", "--version"], 
                         capture_output=True, check=True)
            self.log("✓ yt-dlp encontrado")
        except (subprocess.CalledProcessError, FileNotFoundError):
            self.log("✗ yt-dlp não encontrado")
            self.log("  Instale com: pip install yt-dlp")
        
        try:
            subprocess.run(["ffmpeg", "-version"], 
                         capture_output=True, check=True)
            self.log("✓ ffmpeg encontrado")
        except (subprocess.CalledProcessError, FileNotFoundError):
            self.log("✗ ffmpeg não encontrado")
            self.log("  Instale ffmpeg do site oficial")
    
    def start_download(self):
        url = self.url_var.get().strip()
        
        if not url:
            messagebox.showerror("Erro", "Por favor, insira uma URL!")
            return
        
        if not url.startswith(("http://", "https://")):
            messagebox.showerror("Erro", "URL inválida!")
            return
        
        # Desabilitar botão durante download
        self.download_btn.config(state=tk.DISABLED)
        self.progress_bar.start()
        
        # Executar download em thread separada
        thread = threading.Thread(target=self.download_audio, args=(url,))
        thread.daemon = True
        thread.start()
    
    def download_audio(self, url):
        try:
            output_path = self.download_path.get()
            audio_format = self.format_var.get()
            quality = self.quality_var.get()
            
            self.log(f"\n🎬 Baixando áudio de: {url}")
            self.log(f"📁 Destino: {output_path}")
            self.log(f"🎵 Formato: {audio_format.upper()}")
            
            # Configurar opções do yt-dlp
            output_template = os.path.join(output_path, "%(title)s.%(ext)s")
            
            if audio_format == "mp3":
                # Para MP3
                audio_quality = "0" if quality == "best" else quality
                cmd = [
                    "yt-dlp",
                    "-x",  # Extrair apenas áudio
                    "--audio-format", "mp3",
                    "--audio-quality", audio_quality,
                    "--embed-thumbnail",  # Incluir thumbnail
                    "--add-metadata",  # Adicionar metadados
                    "-o", output_template,
                    url
                ]
            else:
                # Para WAV
                cmd = [
                    "yt-dlp",
                    "-x",
                    "--audio-format", "wav",
                    "-o", output_template,
                    url
                ]
            
            # Executar comando
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            
            # Capturar saída
            for line in process.stdout:
                if "[download]" in line or "[ExtractAudio]" in line:
                    self.log(line.strip())
            
            process.wait()
            
            if process.returncode == 0:
                self.log("✅ Download concluído com sucesso!")
                messagebox.showinfo("Sucesso", "Áudio baixado com sucesso!")
            else:
                self.log("❌ Erro durante o download")
                messagebox.showerror("Erro", "Falha no download. Verifique a URL e sua conexão.")
                
        except Exception as e:
            self.log(f"❌ Erro: {str(e)}")
            messagebox.showerror("Erro", f"Erro durante o download:\n{str(e)}")
        
        finally:
            # Reabilitar botão
            self.progress_bar.stop()
            self.download_btn.config(state=tk.NORMAL)

def main():
    root = tk.Tk()
    app = YouTubeAudioDownloader(root)
    root.mainloop()

if __name__ == "__main__":
    main()
