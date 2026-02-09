# Hypr - Anime Scraper

🎬 **O melhor scraper de animes para terminal!** Busque, selecione e assista seus animes favoritos diretamente no terminal.

## ✨ Funcionalidades

- 🔍 **Busca rápida** de animes
- 🎯 **Interface interativa** com navegação por teclado
- 🎬 **Reprodução automática** no MPV ou navegador
- 🖥️ **Cross-platform** (Linux, macOS, Windows)
- 🚀 **Ultra rápido** e eficiente
- 📱 **Interface moderna** e intuitiva

## 🚀 Instalação Rápida

### Linux/macOS
```bash
curl -fsSL https://raw.githubusercontent.com/inotyu/hypr/main/install.sh | bash
```

### Windows
```bash
# Usando PowerShell
irm https://raw.githubusercontent.com/inotyu/hypr/main/install.sh | bash
```

O script instala automaticamente:
- ✅ Python 3
- ✅ Google Chrome
- ✅ MPV player
- ✅ Todas as dependências

## 📖 Como Usar

```bash
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

# Windows: Baixe de https://python.org

# 3. Criar ambiente virtual (recomendado)
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# 4. Instalar dependências de desenvolvimento
pip install selenium webdriver-manager yt-dlp requests

# Para Windows (interface curses)
pip install windows-curses

# 5. Instalar dependências do sistema
# Linux
sudo apt install mpv google-chrome-stable  # Ubuntu/Debian
sudo dnf install mpv google-chrome-stable   # Fedora
sudo pacman -S mpv google-chrome            # Arch

# macOS
brew install mpv google-chrome

# Windows: Instale MPV e Chrome manualmente

# 6. Testar instalação
python3 -c "import selenium, yt_dlp; print('✅ Dependências OK')"

# 7. Executar
python3 hypr_scraper/hypr naruto
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
├── install.sh          # Script de instalação automática
├── hypr_scraper/
│   ├── hypr            # Executável principal
│   └── src/
│       ├── cli/        # Interface de linha de comando
│       │   ├── interactive.py    # Modo interativo
│       │   └── selector.py       # Seleção com curses
│       └── scraper/   # Módulos de scraping
│           └── hypr_scraper.py   # Scraper principal
└── README.md          # Esta documentação
```

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

- 🐛 Reportar bugs
- 💡 Sugerir melhorias
- 🔧 Enviar pull requests
- 📖 Melhorar a documentação

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## ⚠️ Aviso Legal

Este projeto é apenas para fins educacionais. Use-o apenas para acessar conteúdo que você tem direito de assistir. Os desenvolvedores não se responsabilizam pelo uso indevido.

## 🙏 Créditos

- **Selenium**: Automação web
- **MPV**: Melhor player de vídeo
- **yt-dlp**: Extração de streams

---

**Em desenvolvimento constante.** 🎌
