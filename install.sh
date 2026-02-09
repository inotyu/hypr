#!/bin/bash

# Hypr Anime Scraper - Instalação COMPLETA Universal
# Instala TUDO que precisa para funcionar perfeitamente!

echo "🎬 Hypr Anime Scraper - Instalação COMPLETA"
echo "============================================"
echo "⚠️  ATENÇÃO: Este script instalará:"
echo "   • Python 3 (se necessário)"
echo "   • Google Chrome"
echo "   • MPV player"
echo "   • Todas as dependências"
echo ""
read -p "Continuar? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Instalação cancelada."
    exit 1
fi

# Detectar sistema operacional
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
    # Detectar distribuição Linux
    if command -v apt &> /dev/null; then
        PACKAGE_MANAGER="apt"
        UPDATE_CMD="sudo apt update"
        INSTALL_CMD="sudo apt install -y"
    elif command -v dnf &> /dev/null; then
        PACKAGE_MANAGER="dnf"
        UPDATE_CMD="sudo dnf check-update || true"
        INSTALL_CMD="sudo dnf install -y"
    elif command -v pacman &> /dev/null; then
        PACKAGE_MANAGER="pacman"
        UPDATE_CMD="sudo pacman -Sy"
        INSTALL_CMD="sudo pacman -S --noconfirm"
    elif command -v zypper &> /dev/null; then
        PACKAGE_MANAGER="zypper"
        UPDATE_CMD="sudo zypper refresh"
        INSTALL_CMD="sudo zypper install -y"
    else
        echo "❌ Gerenciador de pacotes não suportado"
        exit 1
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
    if ! command -v brew &> /dev/null; then
        echo "🍺 Instalando Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    OS="windows"
    echo "🪟 Windows detectado. Para instalação completa:"
    echo "1. Instale Python: https://python.org/downloads/"
    echo "2. Instale Google Chrome"
    echo "3. Execute este script novamente"
    echo ""
    echo "Ou use o Scoop para instalação automática:"
    echo "scoop install python mpv googlechrome"
    exit 1
else
    echo "❌ Sistema operacional não suportado: $OSTYPE"
    exit 1
fi

echo "📍 Sistema detectado: $OS"
if [ "$OS" = "linux" ]; then
    echo "📦 Gerenciador de pacotes: $PACKAGE_MANAGER"
fi

# Função para instalar pacotes
install_package() {
    local package=$1
    echo "📦 Instalando $package..."
    
    if [ "$OS" = "linux" ]; then
        $INSTALL_CMD $package || echo "⚠️  Falhou instalar $package (pode já estar instalado)"
    elif [ "$OS" = "macos" ]; then
        brew install $package || echo "⚠️  Falhou instalar $package (pode já estar instalado)"
    fi
}

# Instalar Python se necessário
if ! command -v python3 &> /dev/null; then
    echo "🐍 Instalando Python 3..."
    if [ "$OS" = "linux" ]; then
        case $PACKAGE_MANAGER in
            apt) install_package "python3 python3-pip python3-venv" ;;
            dnf) install_package "python3 python3-pip" ;;
            pacman) install_package "python python-pip" ;;
            zypper) install_package "python3 python3-pip" ;;
        esac
    elif [ "$OS" = "macos" ]; then
        install_package "python3"
    fi
fi

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 ainda não encontrado. Instale manualmente."
    exit 1
fi

echo "✅ Python 3 encontrado: $(python3 --version)"

# Instalar Google Chrome se necessário
if ! command -v google-chrome &> /dev/null && ! command -v google-chrome-stable &> /dev/null && ! command -v chromium-browser &> /dev/null; then
    echo "🌐 Instalando Google Chrome..."
    if [ "$OS" = "linux" ]; then
        case $PACKAGE_MANAGER in
            apt)
                # Adicionar repositório do Chrome
                wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
                echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
                $UPDATE_CMD
                install_package "google-chrome-stable"
                ;;
            dnf)
                # Adicionar repositório do Chrome para Fedora
                sudo dnf config-manager --set-enabled google-chrome
                install_package "google-chrome-stable"
                ;;
            pacman)
                # Chrome no Arch via AUR (simplificado)
                echo "📋 Para Chrome no Arch, execute:"
                echo "   yay -S google-chrome"
                echo "   # ou use Chromium:"
                install_package "chromium"
                ;;
            zypper)
                # Adicionar repositório do Chrome para openSUSE
                sudo zypper addrepo http://dl.google.com/linux/chrome/rpm/stable/x86_64 google-chrome
                sudo zypper refresh
                install_package "google-chrome-stable"
                ;;
        esac
    elif [ "$OS" = "macos" ]; then
        echo "📋 Para macOS, baixe Chrome de: https://google.com/chrome"
        echo "🔄 Continuando instalação..."
    fi
fi

# Instalar MPV player
if ! command -v mpv &> /dev/null; then
    echo "� Instalando MPV player..."
    if [ "$OS" = "linux" ]; then
        case $PACKAGE_MANAGER in
            apt) install_package "mpv" ;;
            dnf) install_package "mpv" ;;
            pacman) install_package "mpv" ;;
            zypper) install_package "mpv" ;;
        esac
    elif [ "$OS" = "macos" ]; then
        install_package "mpv"
    fi
fi

# Instalar yt-dlp
echo "📦 Instalando yt-dlp..."
python3 -m pip install --user yt-dlp || pip3 install --user yt-dlp

# Instalar dependências Python
echo "📦 Instalando dependências Python..."
python3 -m pip install --user selenium webdriver-manager requests

# Biblioteca curses para Windows (não se aplica aqui, mas ok)
if [ "$OS" = "windows" ]; then
    python3 -m pip install --user windows-curses
fi

# Verificar instalação
echo ""
echo "🔍 Verificando instalação..."

errors=0

if ! python3 -c "import selenium" 2>/dev/null; then
    echo "❌ selenium não instalado"
    errors=$((errors+1))
fi

if ! python3 -c "import webdriver_manager" 2>/dev/null; then
    echo "❌ webdriver-manager não instalado" 
    errors=$((errors+1))
fi

if ! command -v yt-dlp &> /dev/null && ! python3 -m yt_dlp --version &> /dev/null; then
    echo "❌ yt-dlp não encontrado"
    errors=$((errors+1))
fi

if [ $errors -eq 0 ]; then
    echo "✅ Todas as dependências instaladas!"
    
    # Criar comando global 'hypr'
    echo "🔗 Criando comando global 'hypr'..."
    
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    HYPR_SCRIPT="$SCRIPT_DIR/hypr_scraper/hypr"
    
    if [ "$OS" = "linux" ] || [ "$OS" = "macos" ]; then
        # Linux/macOS: criar link simbólico
        if sudo ln -sf "$HYPR_SCRIPT" /usr/local/bin/hypr 2>/dev/null; then
            echo "✅ Comando 'hypr' criado em /usr/local/bin/"
        else
            echo "⚠️  Não foi possível criar link simbólico (sudo necessário)"
            echo "💡 Execute: sudo ln -s $HYPR_SCRIPT /usr/local/bin/hypr"
        fi
    elif [ "$OS" = "windows" ]; then
        # Windows: adicionar ao PATH ou criar .bat
        echo "🪟 Windows: Execute o comando abaixo como Administrador:"
        echo "   mklink C:\\Windows\\System32\\hypr.bat \"$HYPR_SCRIPT\""
        echo ""
        echo "Ou adicione ao PATH:"
        echo "   setx PATH \"%PATH%;$SCRIPT_DIR\\hypr_scraper\""
    fi
    
    # Testar comando
    if command -v hypr &> /dev/null; then
        echo ""
        echo "🎉 INSTALAÇÃO COMPLETA! Teste:"
        echo "   hypr naruto"
        echo ""
    else
        echo ""
        echo "⚠️  Comando 'hypr' não está no PATH. Execute:"
        echo "   python3 $HYPR_SCRIPT naruto"
        echo ""
    fi
else
    echo "⚠️  Alguns componentes podem não ter sido instalados corretamente"
fi

echo ""
echo ""
echo "🚀 Como usar:"
echo ""
echo "  # Buscar animes"
echo "  hypr naruto"
echo ""
echo "  # Modo interativo"
echo "  hypr -i"
echo ""
echo "  # Resultados completos"
echo "  hypr -f naruto"
echo ""
echo "📋 O Hypr está pronto para uso!"
echo "🎬 Aproveite seus animes!"
echo ""
echo "� Dica: Se quiser atualizar depois, rode:"
echo "   python3 -m pip install --user --upgrade selenium yt-dlp"
