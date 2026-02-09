# HyprOnline - Anime Scraper

🎬 **O melhor scraper de animes para terminal!** Busque, selecione e assista seus animes favoritos diretamente no terminal.

## ✨ Funcionalidades

- 🔍 **Busca rápida** de animes
- 🎯 **Interface interativa** com navegação por teclado
- 🎬 **Reprodução automática** no MPV ou navegador
- 🖥️ **Cross-platform** (Linux, macOS, Windows)
- 🚀 **Ultra rápido** e eficiente
- 📱 **Interface moderna** e intuitiva

## 🚀 Instalação Rápida

### 🐧 Linux / 🍎 macOS
```bash
curl -fsSL https://raw.githubusercontent.com/inotyu/hypr/main/install.sh | bash
```

### 🪟 Windows
```powershell
# PowerShell como Administrador
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
irm https://raw.githubusercontent.com/inotyu/hypr/main/install.ps1 | iex
```

O script instala automaticamente:
- ✅ Python 3
- ✅ Google Chrome
- ✅ MPV player
- ✅ Todas as dependências

## 📖 Como Usar

### 🐧 Linux / 🍎 macOS
```bash
# Buscar animes
hypr naruto

# Modo interativo forçado
hypr -i

# Resultados completos (sem interface)
hypr -f naruto
```

### 🪟 Windows
```powershell
# Buscar animes
hypr naruto

# Modo interativo forçado
hypr -i

# Resultados completos (sem interface)
hypr -f naruto
```

### Controles da Interface

- **W/S** ou **↑/↓**: Navegar entre opções
- **Enter**: Selecionar anime/episódio ou reproduzir vídeo
- **Q**: Sair

## 🎯 Funcionalidades Avançadas

- **Busca inteligente**: Encontra animes por nome parcial
- **Reprodução automática**: Abre no MPV ou navegador
- **Fallback inteligente**: Se MPV falhar, abre no navegador
- **Cache otimizado**: Baixa apenas o necessário
- **Atualizações automáticas**: Sempre usa as últimas versões

## 🛠️ Desenvolvimento

### 📥 Clonando e Configurando

#### 🐧 Linux / 🍎 macOS
```bash
# 1. Clonar o repositório
git clone https://github.com/inotyu/hypr.git
cd hypr

# 2. Instalar Python (se necessário)
# Linux
sudo apt install python3 python3-pip python3-venv  # Ubuntu/Debian
sudo dnf install python3 python3-pip              # Fedora
sudo pacman -S python python-pip                  # Arch

# macOS
brew install python3

# 3. Criar ambiente virtual (recomendado)
python3 -m venv venv
source venv/bin/activate

# 4. Instalar dependências
pip install selenium webdriver-manager yt-dlp requests

# 5. Instalar dependências do sistema
sudo apt install mpv google-chrome-stable  # Ubuntu/Debian
sudo dnf install mpv google-chrome-stable   # Fedora
sudo pacman -S mpv google-chrome            # Arch
# macOS
brew install mpv google-chrome

# 6. Testar instalação
python3 -c "import selenium, yt_dlp; print('✅ Dependências OK')"

# 7. Executar
python3 hypr_scraper/hypr naruto
```

#### 🪟 Windows
```powershell
# 1. Clonar o repositório
git clone https://github.com/inotyu/hypr.git
cd hypr

# 2. Instalar Python (baixe de python.org)
# Verifique a opção "Add Python to PATH"

# 3. Criar ambiente virtual (recomendado)
python -m venv venv
venv\Scripts\activate

# 4. Instalar dependências
pip install selenium webdriver-manager yt-dlp requests windows-curses

# 5. Instalar dependências do sistema
# Google Chrome: google.com/chrome
# MPV Player: mpv.io ou via Chocolatey/Scoop
choco install mpv
# ou
scoop install mpv

# 6. Testar instalação
python -c "import selenium, yt_dlp; print('✅ Dependências OK')"

# 7. Executar
python hypr_scraper/hypr naruto
```

### 🔧 Estrutura para Modificações

```bash
# Arquivos principais para modificar:
hypr_scraper/src/scraper/hypr_scraper.py    # Lógica de scraping
hypr_scraper/src/cli/selector.py            # Interface interativa
hypr_scraper/src/cli/interactive.py         # Modo interativo
hypr_scraper/hypr                          # Script principal
```

### 🧪 Testando Modificações

```bash
# Testar scraping
python3 -c "from hypr_scraper.src.scraper.hypr_scraper import HyprScraper; s = HyprScraper(); print('Teste OK')"

# Testar interface
python3 hypr_scraper/hypr -i

# Testar busca
python3 hypr_scraper/hypr naruto
```

### 📤 Enviando Modificações

```bash
# 1. Criar branch para sua modificação
git checkout -b feature-sua-ideia

# 2. Fazer modificações
# ... edite os arquivos ...

# 3. Testar mudanças
python3 hypr_scraper/hypr naruto

# 4. Commit
git add .
git commit -m "✨ Adicionada nova funcionalidade: descrição"

# 5. Push
git push origin feature-sua-ideia

# 6. Criar Pull Request no GitHub
```

## 📋 Estrutura do Projeto

```
hypr/
├── install.sh          # Script de instalação Linux/macOS
├── install.ps1         # Script de instalação Windows
├── WINDOWS_SETUP.md    # Guia detalhado Windows
├── README.md           # Este arquivo
├── hypr_scraper/
│   ├── hypr            # Executável principal
│   └── src/
│       ├── cli/        # Interface de linha de comando
│       │   ├── interactive.py    # Modo interativo
│       │   └── selector.py       # Seleção com curses
│       ├── scraper/     # Lógica de web scraping
│       │   └── hypr_scraper.py   # Scraper principal
│       ├── models/      # Models de dados
│       │   ├── anime.py         # Modelo Anime
│       │   └── episode.py       # Modelo Episode
│       └── utils/       # Utilitários
│           └── exceptions.py     # Exceções customizadas
└── requirements.txt    # Dependências Python
```

## 🔗 Links Úteis

### 📖 Guias Específicos
- **[🪟 Windows Setup Guide](WINDOWS_SETUP.md)** - Guia completo para Windows
- **[🐧 Linux/macOS](install.sh)** - Script de instalação automática

### 🛠️ Dependências
- **[Python 3.11+](https://www.python.org/downloads/)** - Linguagem principal
- **[Google Chrome](https://www.google.com/chrome/)** - Navegador para scraping
- **[MPV Player](https://mpv.io/)** - Reprodutor de vídeo recomendado

### 📦 Gerenciadores de Pacotes
- **[Chocolatey (Windows)](https://chocolatey.org/)** - `choco install mpv`
- **[Scoop (Windows)](https://scoop.sh/)** - `scoop install mpv`
- **[Homebrew (macOS)](https://brew.sh/)** - `brew install mpv`

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor:

1. **Faça um Fork** do projeto
2. **Crie uma Branch** para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit suas mudanças** (`git commit -m 'Add some AmazingFeature'`)
4. **Push para a Branch** (`git push origin feature/AmazingFeature`)
5. **Abra um Pull Request**

## 📝 Licença

Este projeto está sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🐛 Problemas e Suporte

- **[Abrir Issue](https://github.com/inotyu/hypr/issues)** - Reportar bugs
- **[Discussions](https://github.com/inotyu/hypr/discussions)** - Dúvidas e sugestões
- **[Wiki](https://github.com/inotyu/hypr/wiki)** - Documentação adicional

---

⭐ **Se este projeto ajudou você, deixe uma estrela!**
