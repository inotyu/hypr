# Hypr Anime Scraper - Script de Instalação para Windows
# Execute no PowerShell como Administrador

Write-Host "🎬 Hypr Anime Scraper - Instalação para Windows" -ForegroundColor Cyan
Write-Host "=================================================" -ForegroundColor Cyan

# Verificar se está executando como Administrador
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "❌ Execute este script como Administrador!" -ForegroundColor Red
    pause
    exit 1
}

# Verificar PowerShell versão
if ($PSVersionTable.PSVersion.Major -lt 5) {
    Write-Host "❌ PowerShell 5.0 ou superior é necessário!" -ForegroundColor Red
    pause
    exit 1
}

Write-Host "🔍 Verificando pré-requisitos..." -ForegroundColor Yellow

# 1. Verificar/Instalar Python
Write-Host "📦 Verificando Python..." -ForegroundColor Green
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "⬇️ Baixando Python..." -ForegroundColor Blue
    Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe" -OutFile "$env:TEMP\python-installer.exe"
    Write-Host "🚀 Instalando Python (aguarde o instalador GUI)..." -ForegroundColor Blue
    Start-Process "$env:TEMP\python-installer.exe" -Wait
    Remove-Item "$env:TEMP\python-installer.exe" -Force
} else {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python encontrado: $pythonVersion" -ForegroundColor Green
}

# 2. Verificar/Instalar Google Chrome
Write-Host "🌐 Verificando Google Chrome..." -ForegroundColor Green
$chrome = Get-Command chrome -ErrorAction SilentlyContinue
if (-not $chrome) {
    Write-Host "⬇️ Baixando Google Chrome..." -ForegroundColor Blue
    Invoke-WebRequest -Uri "https://dl.google.com/chrome/install/latest/chrome_installer.exe" -OutFile "$env:TEMP\chrome-installer.exe"
    Write-Host "🚀 Instalando Chrome..." -ForegroundColor Blue
    Start-Process "$env:TEMP\chrome-installer.exe" -Wait -ArgumentList "/silent", "/install"
    Remove-Item "$env:TEMP\chrome-installer.exe" -Force
} else {
    Write-Host "✅ Google Chrome encontrado" -ForegroundColor Green
}

# 3. Instalar MPV Player
Write-Host "🎥 Instalando MPV Player..." -ForegroundColor Green
if (-not (Get-Command mpv -ErrorAction SilentlyContinue)) {
    Write-Host "⬇️ Baixando MPV..." -ForegroundColor Blue
    $mpvPath = "$env:PROGRAMFILES\MPV"
    if (-not (Test-Path $mpvPath)) {
        New-Item -ItemType Directory -Path $mpvPath -Force | Out-Null
    }
    Invoke-WebRequest -Uri "https://sourceforge.net/projects/mpv-player-windows/files/64bit/mpv-x86_64-20230705-git-0e7e084.7z/download" -OutFile "$env:TEMP\mpv.7z"
    
    # Baixar 7-Zip se não tiver
    if (-not (Get-Command 7z -ErrorAction SilentlyContinue)) {
        Write-Host "⬇️ Baixando 7-Zip..." -ForegroundColor Blue
        Invoke-WebRequest -Uri "https://www.7-zip.org/a/7z2201-x64.exe" -OutFile "$env:TEMP\7z-installer.exe"
        Start-Process "$env:TEMP\7z-installer.exe" -Wait -ArgumentList "/S"
        Remove-Item "$env:TEMP\7z-installer.exe" -Force
    }
    
    # Extrair MPV
    Write-Host "📦 Extraindo MPV..." -ForegroundColor Blue
    & 7z x "$env:TEMP\mpv.7z" "-o$mpvPath" -y
    Move-Item "$mpvPath\mpv-x86_64-*\*" "$mpvPath\" -Force
    Remove-Item "$mpvPath\mpv-x86_64-*" -Recurse -Force
    Remove-Item "$env:TEMP\mpv.7z" -Force
    
    # Adicionar ao PATH
    $currentPath = [Environment]::GetEnvironmentVariable("PATH", "Machine")
    if ($currentPath -notlike "*$mpvPath*") {
        [Environment]::SetEnvironmentVariable("PATH", "$currentPath;$mpvPath", "Machine")
        $env:PATH += ";$mpvPath"
    }
} else {
    Write-Host "✅ MPV Player encontrado" -ForegroundColor Green
}

# 4. Clonar o repositório
Write-Host "📥 Clonando repositório Hypr..." -ForegroundColor Green
$installPath = "$env:USERPROFILE\hypr"
if (Test-Path $installPath) {
    Write-Host "📁 Removendo instalação anterior..." -ForegroundColor Yellow
    Remove-Item $installPath -Recurse -Force
}

Set-Location $env:USERPROFILE
git clone https://github.com/inotyu/hypr.git
Set-Location hypr

# 5. Instalar dependências Python
Write-Host "🐍 Instalando dependências Python..." -ForegroundColor Green
python -m pip install --upgrade pip
pip install selenium webdriver-manager requests yt-dlp

# 6. Criar script executável do Windows
Write-Host "🔧 Criando script hypr.ps1..." -ForegroundColor Green
$hyprScript = @"
# Hypr Anime Scraper - Script Principal para Windows
param(
    [Parameter(ValueFromRemainingArguments=`$true)]
    [string[]]`$args
)

# Adicionar diretório ao PATH
`$scriptPath = Split-Path -Parent `$MyInvocation.MyCommand.Path
`$env:PYTHONPATH = "`$scriptPath\src"

# Executar o script Python
python "`$scriptPath\hypr" `$args
"@

Set-Content -Path "hypr.ps1" -Value $hyprScript -Encoding UTF8

# 7. Criar atalho global
Write-Host "🔗 Criando atalho global 'hypr'..." -ForegroundColor Green
$shortcutPath = "$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\hypr.lnk"
$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = "powershell.exe"
$shortcut.Arguments = "-ExecutionPolicy Bypass -File `"$installPath\hypr.ps1`""
$shortcut.WorkingDirectory = $installPath
$shortcut.IconLocation = "powershell.exe,0"
$shortcut.Save()

# 8. Adicionar ao PATH do sistema
Write-Host "🛤️ Adicionando ao PATH do sistema..." -ForegroundColor Green
$currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($currentPath -notlike "*$installPath*") {
    [Environment]::SetEnvironmentVariable("PATH", "$currentPath;$installPath", "User")
    $env:PATH += ";$installPath"
}

Write-Host ""
Write-Host "🎉 Instalação concluída com sucesso!" -ForegroundColor Green
Write-Host ""
Write-Host "📖 Como usar:" -ForegroundColor Cyan
Write-Host "  Abra um NOVO terminal e execute:" -ForegroundColor White
Write-Host "  hypr 'nome do anime'" -ForegroundColor Yellow
Write-Host ""
Write-Host "🔧 Para testar:" -ForegroundColor Cyan
Write-Host "  hypr naruto" -ForegroundColor Yellow
Write-Host ""
Write-Host "⚠️ Importante: Feche e abra um novo terminal para as alterações PATH funcionarem!" -ForegroundColor Red
Write-Host ""

pause
