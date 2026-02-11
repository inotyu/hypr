#!/bin/bash

# Hypr Anime Scraper - Instalação Simplificada
# Versão sem prompt interativo

echo "=================================="
echo "Hypr Anime Scraper - Instalacao"
echo "=================================="
echo ""
echo "Instalando dependencias..."
echo ""

# Detectar Arch Linux
if ! command -v pacman &> /dev/null; then
    echo "ERRO: Este script é para Arch Linux"
    exit 1
fi

# Instalar dependências do sistema
echo "[1/5] Instalando pacotes do sistema..."
sudo pacman -S --noconfirm python python-pip mpv chromium git

# Instalar dependências Python
echo "[2/5] Instalando dependencias Python..."
python3 -m pip install --break-system-packages selenium webdriver-manager requests yt-dlp beautifulsoup4 html5lib

# Clonar repositório
echo "[3/5] Clonando repositorio..."
cd ~
if [ -d "hypr" ]; then
    echo "Diretorio hypr ja existe, pulando clone..."
    cd hypr
    git pull
else
    git clone https://github.com/inotyu/hypr.git
    cd hypr
fi

# Tornar executável
echo "[4/5] Configurando permissoes..."
chmod +x hypr_scraper/hypr

# Criar link simbólico
echo "[5/5] Criando comando global..."
sudo ln -sf "$(pwd)/hypr_scraper/hypr" /usr/local/bin/hypr

# Adicionar PYTHONPATH ao .bashrc para evitar problemas de importação
echo "[6/6] Configurando PYTHONPATH..."
if ! grep -q "PYTHONPATH.*hypr" ~/.bashrc; then
    echo "export PYTHONPATH=\$PYTHONPATH:$(pwd)" >> ~/.bashrc
fi
export PYTHONPATH=$PYTHONPATH:$(pwd)

echo ""
echo "=================================="
echo "INSTALACAO COMPLETA!"
echo "=================================="
echo ""
echo "Teste agora:"
echo "  hypr naruto"
echo ""
