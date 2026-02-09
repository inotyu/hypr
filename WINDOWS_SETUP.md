# 🪟 Hypr Anime Scraper - Guia de Instalação Windows

## 📋 Pré-requisitos
- Windows 10 ou 11
- PowerShell 5.0+ (já vem com o Windows)
- Conexão com internet
- Permissões de Administrador

## 🚀 Instalação Automática (Recomendado)

1. **Baixe o script de instalação:**
   ```powershell
   # Abra PowerShell como Administrador
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
   Invoke-WebRequest -Uri "https://raw.githubusercontent.com/inotyu/hypr/main/install.ps1" -OutFile "$env:TEMP\install.ps1"
   ```

2. **Execute a instalação:**
   ```powershell
   # No PowerShell como Administrador
   & "$env:TEMP\install.ps1"
   ```

3. **Aguarde a instalação completar** (pode levar alguns minutos)

## 🛠️ Instalação Manual

### 1. Instalar Python
```powershell
# Baixe e instale Python 3.11+ de python.org
# Durante a instalação, marque "Add Python to PATH"
```

### 2. Instalar Google Chrome
```powershell
# Baixe e instale de google.com/chrome
```

### 3. Instalar MPV Player
```powershell
# Baixe de mpv.io ou via Chocolatey:
choco install mpv
# ou via Scoop:
scoop install mpv
```

### 4. Clonar o Repositório
```powershell
git clone https://github.com/inotyu/hypr.git $env:USERPROFILE\hypr
cd $env:USERPROFILE\hypr
```

### 5. Instalar Dependências Python
```powershell
python -m pip install --upgrade pip
pip install selenium webdriver-manager requests yt-dlp
```

### 6. Criar Script Executável
Crie o arquivo `hypr.ps1` na pasta do projeto:
```powershell
# Hypr Anime Scraper - Script Principal para Windows
param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$args
)

# Adicionar diretório ao PATH
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$env:PYTHONPATH = "$scriptPath\src"

# Executar o script Python
python "$scriptPath\hypr" $args
```

### 7. Adicionar ao PATH
```powershell
# Adicione a pasta do hypr ao PATH do sistema
# Painel de Controle > Sistema > Variáveis de Ambiente
# Edite PATH e adicione: %USERPROFILE%\hypr
```

## 📖 Como Usar

Após a instalação, abra um **NOVO** terminal e execute:

```powershell
# Buscar um anime
hypr naruto

# Buscar com nome completo
hypr "attack on titan"

# Ver todos os resultados
hypr one piece --full
```

## 🎮 Controles no Modo Interativo

- **↑/↓** - Navegar pela lista
- **Enter** - Selecionar/Reproduzir
- **q** - Sair
- **Esc** - Cancelar

## 🔧 Players de Vídeo

O script tentará usar nesta ordem:
1. **MPV** (recomendado)
2. **VLC** (se instalado)
3. **Browser padrão** (fallback)

## 🐛 Solução de Problemas

### "Comando não encontrado"
```powershell
# Verifique se o hypr está no PATH
where hypr

# Se não encontrar, adicione manualmente:
$env:PATH += ";$env:USERPROFILE\hypr"
```

### "Python não encontrado"
```powershell
# Verifique instalação do Python
python --version

# Se não tiver, instale de python.org
```

### Erro de ChromeDriver
```powershell
# Reinstale as dependências
pip uninstall webdriver-manager
pip install webdriver-manager --upgrade
```

### Vídeo não reproduz
```powershell
# Teste o MPV manualmente
mpv "https://example.com/video.mp4"

# Se não funcionar, instale via:
choco install mpv
# ou
scoop install mpv
```

## 🔄 Atualizar

Para atualizar para a versão mais recente:
```powershell
cd $env:USERPROFILE\hypr
git pull origin main
pip install -r requirements.txt --upgrade
```

## 📁 Estrutura de Arquivos

```
%USERPROFILE%\hypr\
├── hypr                 # Script Python principal
├── hypr.ps1            # Script PowerShell
├── hypr_scraper\       # Código fonte
│   ├── src\
│   │   ├── scraper\    # Web scraping
│   │   ├── cli\        # Interface
│   │   └── models\     # Models
│   └── requirements.txt
└── WINDOWS_SETUP.md    # Este arquivo
```

## 🆘 Suporte

Se encontrar problemas:

1. **Verifique os pré-requisitos** (Python, Chrome, MPV)
2. **Execute como Administrador** se houver erros de permissão
3. **Abra nova janela do PowerShell** após a instalação
4. **Verifique o PATH** do sistema

## 📝 Notas Importantes

- Execute o PowerShell como **Administrador** durante a instalação
- **Feche e abra** o terminal após a instalação para atualizar o PATH
- O MPV é o player mais recomendado para melhor performance
- Chrome é necessário para o web scraping funcionar

---

🎬 **Divirta-se assistindo seus animes favoritos!**
