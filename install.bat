@echo off
chcp 65001 >nul
title Hypr Anime Scraper - Instalador

echo ==================================
echo Hypr Anime Scraper - Instalador
echo ==================================
echo.
echo Instalando dependencias...
echo.

REM Verificar se Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [1/6] Python nao encontrado. Instalando...
    winget install Python.Python.3.12 --accept-source-agreements --accept-package-agreements --force
    if errorlevel 1 (
        echo ERRO: Nao foi possivel instalar Python automaticamente
        echo Por favor, instale Python manualmente de https://python.org
        pause
        exit /b 1
    )
    REM Atualizar PATH para incluir Python
    set PATH=%PATH%;%LOCALAPPDATA%\Programs\Python\Python312\Scripts;%LOCALAPPDATA%\Programs\Python\Python312
) else (
    echo [1/6] Python ja instalado
)

REM Verificar se Git esta instalado
git --version >nul 2>&1
if errorlevel 1 (
    echo [2/6] Git nao encontrado. Instalando...
    winget install Git.Git --accept-source-agreements --accept-package-agreements --force
    if errorlevel 1 (
        echo ERRO: Nao foi possivel instalar Git automaticamente
        pause
        exit /b 1
    )
) else (
    echo [2/6] Git ja instalado
)

REM Verificar se Chrome/Chromium esta instalado
where chrome >nul 2>&1
if errorlevel 1 (
    where chromium >nul 2>&1
    if errorlevel 1 (
        echo [3/6] Chrome/Chromium nao encontrado. Instalando Chrome...
        winget install Google.Chrome --accept-source-agreements --accept-package-agreements --force
        if errorlevel 1 (
            echo ERRO: Nao foi possivel instalar Chrome automaticamente
            pause
            exit /b 1
        )
    ) else (
        echo [3/6] Chromium ja instalado
    )
) else (
    echo [3/6] Chrome ja instalado
)

REM Verificar se MPV esta instalado
mpv --version >nul 2>&1
if errorlevel 1 (
    echo [4/6] MPV nao encontrado. Instalando...
    winget install MPV.MPV --accept-source-agreements --accept-package-agreements --force
    if errorlevel 1 (
        echo Tentando instalar via Scoop...
        powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser; irm get.scoop.sh | iex"
        scoop install mpv
        if errorlevel 1 (
            echo ERRO: Nao foi possivel instalar MPV automaticamente
            echo Por favor, instale MPV manualmente de https://mpv.io
            pause
            exit /b 1
        )
    )
) else (
    echo [4/6] MPV ja instalado
)

REM Clonar ou atualizar repositorio
echo [5/6] Configurando Hypr...
if exist "hypr" (
    echo Diretorio hypr ja existe, atualizando...
    cd hypr
    git pull
) else (
    echo Clonando repositorio...
    git clone https://github.com/inotyu/hypr.git
    cd hypr
)

REM Instalar dependencias Python
echo [6/6] Instalando dependencias Python...
python -m pip install --user --upgrade selenium webdriver-manager requests yt-dlp

REM Verificar se yt-dlp esta acessivel
yt-dlp --version >nul 2>&1
if errorlevel 1 (
    echo Configurando yt-dlp no PATH...
    set PATH=%PATH%;%LOCALAPPDATA%\Programs\Python\Python312\Scripts
)

REM Criar atalho desktop
echo Criando atalho no desktop...
powershell -Command ^
"$WshShell = New-Object -comObject WScript.Shell; ^
$Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\Hypr Anime Scraper.lnk'); ^
$Shortcut.TargetPath = '%CD%\hypr.bat'; ^
$Shortcut.WorkingDirectory = '%CD%'; ^
$Shortcut.IconLocation = '%CD%\logo.jpg'; ^
$Shortcut.Description = 'Hypr Anime Scraper - Assistir animes online'; ^
$Shortcut.Save()"

REM Criar script hypr.bat
echo Criando script de inicializacao...
(
echo @echo off
echo cd /d "%%~dp0"
echo python hypr_scraper\hypr %%*
) > hypr.bat

REM Criar icone a partir da logo
echo Criando icone a partir da logo...
powershell -Command ^
"Add-Type -AssemblyName System.Drawing; ^
try { ^
    $img = [System.Drawing.Image]::FromFile((Resolve-Path '%CD%\logo.jpg')); ^
    $bitmap = New-Object System.Drawing.Bitmap($img, 64, 64); ^
    $icon = [System.Drawing.Icon]::FromHandle($bitmap.GetHicon()); ^
    $fileStream = New-Object System.IO.FileStream('%CD%\icon.ico', [System.IO.FileMode]::Create); ^
    $icon.Save($fileStream); ^
    $fileStream.Close(); ^
    Write-Host 'Icon created successfully'; ^
} catch { ^
    Write-Host 'Using fallback icon'; ^
    Copy-Item '%CD%\logo.jpg' '%CD%\icon.ico'; ^
}"

echo.
echo ==================================
echo INSTALACAO COMPLETA!
echo ==================================
echo.
echo Atalho criado no desktop: "Hypr Anime Scraper"
echo.
echo Teste agora:
echo   - Clique no atalho do desktop
echo   - Ou execute: hypr "nome do anime"
echo.
echo Exemplos:
echo   hypr naruto
echo   hypr "kaoru hana"
echo.
pause
