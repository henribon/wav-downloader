# 🎵 YouTube Audio Downloader

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

Aplicação web e desktop para baixar áudio de vídeos do YouTube em formato MP3 ou WAV com qualidade máxima.

## 🌐 Versão Web (Recomendada)

Interface web minimalista e moderna para baixar áudios diretamente pelo navegador!

## ⚠️ Aviso Legal

**Use apenas para conteúdo que você tem direito de baixar!**

Este software é fornecido apenas para fins educacionais e para uso com conteúdo do qual você possui os direitos ou permissão explícita para baixar. Respeite os direitos autorais e os termos de serviço do YouTube.

## ✨ Recursos

- 🎵 **Múltiplos Formatos**: Baixe em MP3 (compacto) ou WAV (qualidade máxima)
- ⚡ **Interface Gráfica Intuitiva**: Interface amigável construída com Tkinter
- 🎚️ **Controle de Qualidade**: Escolha a qualidade do MP3 (best, 320k, 256k, 192k, 128k)
- 📁 **Escolha o Destino**: Selecione onde salvar seus arquivos
- 🖼️ **Metadados Automáticos**: Inclui thumbnail e metadados (MP3)
- 📊 **Log em Tempo Real**: Acompanhe o progresso do download
- 🔍 **Verificação de Dependências**: Verifica automaticamente se as ferramentas necessárias estão instaladas

## 📸 Screenshots

```
╔════════════════════════════════════════╗
║   🎵 YouTube Audio Downloader          ║
╠════════════════════════════════════════╣
║                                        ║
║  URL do vídeo:                         ║
║  ┌──────────────────────────────────┐  ║
║  │ https://youtube.com/watch?v=...  │  ║
║  └──────────────────────────────────┘  ║
║                                        ║
║  Formato: ○ MP3 ● WAV                  ║
║  Qualidade MP3: [best ▼]               ║
║                                        ║
║  Pasta de destino:                     ║
║  [~/Downloads] [Procurar...]           ║
║                                        ║
║          [⬇ Baixar Áudio]              ║
║                                        ║
║  Log:                                  ║
║  ┌──────────────────────────────────┐  ║
║  │ ✓ yt-dlp encontrado              │  ║
║  │ ✓ ffmpeg encontrado              │  ║
║  └──────────────────────────────────┘  ║
╚════════════════════════════════════════╝
```

## 📥 Instalação e Uso

### 🌐 Versão Web (Simples e Rápida)

1. **Clone o Repositório**
```bash
git clone https://github.com/seu-usuario/wav-downloader.git
cd wav-downloader
```

2. **Instale as Dependências**
```bash
pip install -r requirements.txt
```

3. **Instale o FFmpeg** (veja instruções abaixo)

4. **Inicie o Servidor**
```bash
python app.py
```

5. **Abra no Navegador**
```
http://localhost:5000
```

Pronto! Agora é só colar a URL do YouTube e clicar em Download! 🎉

---

### 💻 Versão Desktop (Interface Gráfica Tkinter)

Se preferir usar a versão desktop com interface gráfica:

```bash
python youtube_audio_downloader.py
```

---

### 🔧 Instalação do FFmpeg

O FFmpeg é necessário para converter os arquivos de áudio.

#### Windows

1. Baixe do [site oficial do FFmpeg](https://ffmpeg.org/download.html)
2. Extraia o arquivo ZIP
3. Adicione a pasta `bin` ao PATH do sistema
4. Verifique a instalação: `ffmpeg -version`

#### Linux

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Fedora:**
```bash
sudo dnf install ffmpeg
```

**Arch Linux:**
```bash
sudo pacman -S ffmpeg
```

#### macOS

```bash
brew install ffmpeg
```

## 🚀 Como Usar a Versão Web

1. **Inicie o servidor** com `python app.py`
2. **Abra o navegador** em `http://localhost:5000`
3. **Cole a URL do vídeo do YouTube** no campo de texto
4. **Escolha o formato**:
   - **MP3**: Formato comprimido, arquivos menores
   - **WAV**: Formato sem compressão, máxima qualidade
5. **Clique em "Download"** e aguarde
6. O arquivo será baixado automaticamente para seu computador!

### Como Usar a Versão Desktop

1. Execute `python youtube_audio_downloader.py`
2. Cole a URL do vídeo
3. Escolha o formato e qualidade
4. Selecione a pasta de destino
5. Clique em "Baixar Áudio"

## 🛠️ Tecnologias Utilizadas

- **Python 3.7+**: Linguagem de programação
- **Flask**: Framework web para a interface online
- **Tkinter**: Interface gráfica desktop (incluído no Python)
- **yt-dlp**: Biblioteca para download de vídeos/áudio do YouTube
- **FFmpeg**: Conversão e processamento de áudio

## 📋 Requisitos do Sistema

- Python 3.7 ou superior
- FFmpeg instalado e disponível no PATH
- Conexão com a internet
- Sistema operacional: Windows, Linux ou macOS

## 🔧 Solução de Problemas

### O programa não inicia

- Verifique se o Python 3.7+ está instalado: `python --version`
- Certifique-se de que o Tkinter está instalado (geralmente vem com Python)

### Erro: "yt-dlp não encontrado"

```bash
pip install --upgrade yt-dlp
```

### Erro: "ffmpeg não encontrado"

- Verifique se o FFmpeg está instalado: `ffmpeg -version`
- No Windows, certifique-se de que o FFmpeg está no PATH do sistema
- Reinicie o terminal/prompt após instalar o FFmpeg

### Download falha ou trava

- Verifique sua conexão com a internet
- Certifique-se de que a URL do vídeo é válida
- Alguns vídeos podem ter restrições de download
- Atualize o yt-dlp: `pip install --upgrade yt-dlp`

### Arquivo baixado sem som

- Verifique se o FFmpeg está instalado corretamente
- Tente baixar em um formato diferente (MP3 ou WAV)

## 📝 Diferenças entre MP3 e WAV

| Característica | MP3 | WAV |
|---------------|-----|-----|
| **Compressão** | Com perda | Sem compressão |
| **Tamanho do arquivo** | Pequeno (~3-5 MB por música) | Grande (~30-50 MB por música) |
| **Qualidade** | Boa (dependendo do bitrate) | Máxima (áudio original) |
| **Uso recomendado** | Audição casual, armazenamento | Edição, produção musical |
| **Compatibilidade** | Universal | Universal |
| **Metadados** | Suportado | Limitado |

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto é fornecido "como está", sem garantias. Use por sua conta e risco.

## 🙏 Agradecimentos

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Ferramenta poderosa de download
- [FFmpeg](https://ffmpeg.org/) - Processamento multimídia
- Comunidade Python

## 📧 Contato

Se você tiver dúvidas ou sugestões, abra uma [issue](https://github.com/seu-usuario/wav-downloader/issues) no GitHub.

---

**Lembre-se**: Sempre respeite os direitos autorais e use esta ferramenta de forma responsável! 🎵
