# 🚀 Como Usar - Guia Rápido

## 📋 Pré-requisitos

Antes de começar, você precisa ter instalado:

1. **Python 3.7+**
   ```bash
   python --version
   ```

2. **FFmpeg** (obrigatório!)
   - Windows: Baixe de https://ffmpeg.org/download.html e adicione ao PATH
   - Linux: `sudo apt install ffmpeg`
   - macOS: `brew install ffmpeg`

   Verifique: `ffmpeg -version`

3. **Dependências Python**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Passo a Passo

### 1. Iniciar o Servidor

```bash
python app.py
```

Você deve ver:
```
==================================================
🎵 YouTube Audio Downloader Server
==================================================
Pasta de downloads: /tmp/...
Servidor rodando em: http://127.0.0.1:5000
Pressione Ctrl+C para parar
==================================================
✓ yt-dlp encontrado
✓ ffmpeg encontrado
==================================================
```

⚠️ **IMPORTANTE**: Deixe este terminal ABERTO! O servidor precisa ficar rodando.

### 2. Abrir no Navegador

Abra em um **NOVO** terminal ou navegador:
```
http://localhost:5000
```

### 3. Usar a Interface

1. Cole a URL do vídeo do YouTube
2. Escolha MP3 ou WAV
3. Clique em Download
4. Aguarde o processamento

## 🐛 Troubleshooting

### "Nada acontece quando clico em Download"

1. **Verifique se o servidor está rodando**
   ```bash
   python test_server.py
   ```

2. **Abra o Console do Navegador**
   - Pressione F12
   - Vá na aba "Console"
   - Clique em Download novamente
   - Veja se aparece algum erro

3. **Verifique o Terminal**
   - Olhe o terminal onde rodou `python app.py`
   - Deve aparecer logs quando você clica em Download

### Erro: "Servidor não está rodando"

```bash
# Verifique se o servidor está ativo
python test_server.py

# Se não estiver, inicie:
python app.py
```

### Erro: "yt-dlp não encontrado"

```bash
pip install --upgrade yt-dlp
```

### Erro: "ffmpeg não encontrado"

Instale o FFmpeg:
- Windows: https://ffmpeg.org/download.html
- Linux: `sudo apt install ffmpeg`
- macOS: `brew install ffmpeg`

### Download demora muito

- Vídeos longos podem demorar 1-5 minutos
- Aguarde até aparecer a mensagem de sucesso
- Veja o progresso no terminal do servidor

## 📞 Ainda não funciona?

1. Feche tudo (navegador e servidor)
2. Inicie o servidor novamente: `python app.py`
3. Abra um navegador NOVO em: http://localhost:5000
4. Abra o Console (F12) e tente novamente
5. Me envie:
   - O que aparece no Console do navegador (F12)
   - O que aparece no terminal do servidor
   - A URL que você está tentando baixar

## 💡 Exemplo de Uso

```
Terminal 1:
$ python app.py
🎵 YouTube Audio Downloader Server
Servidor rodando em: http://127.0.0.1:5000
...

Navegador:
1. Abrir http://localhost:5000
2. Colar: https://www.youtube.com/watch?v=dQw4w9WgXcQ
3. Escolher: MP3
4. Clicar: Download
5. Aguardar...
6. Arquivo baixa automaticamente!
```
