<div align="center">

<img src="hypr_scraper/src/file_00000000996871f59d54ec96a1919c08.png" alt="HyprOnline" width="600"/>

# HyprOnline

**Scraper de animes para terminal**

HyprOnline é um scraper de animes que permite buscar, navegar e reproduzir conteúdo diretamente do terminal. Utilizando interface baseada em curses/ncurses, oferece navegação por teclado e integração nativa com o MPV player.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)

[Instalação](#-instalação) • [Como Usar](#-como-usar) • [Roadmap](#-roadmap)

</div>

---

## ✨ Funcionalidades

🔍 **Busca inteligente** - Sistema de busca fuzzy que suporta nomes parciais

🎯 **Interface interativa** - Navegação via teclado (setas ou WASD)

🎬 **Reprodução integrada** - Suporte para MPV player e fallback para navegador

⚡ **Performance otimizada** - Sistema de cache para buscas frequentes

🖥️ **Multiplataforma** - Suporte completo para Linux, macOS e Windows

🎨 **Interface minimalista** - Design limpo sem elementos desnecessários

---

## 🚀 Instalação

### Linux

#### 🐧 **Instalação Automática**

[![Download Linux](https://img.shields.io/badge/Download-Linux-FCC624?style=for-the-badge&logo=linux&logoColor=white)](https://raw.githubusercontent.com/inotyu/hypr/main/install.sh)

```bash
curl -fsSL https://raw.githubusercontent.com/inotyu/hypr/main/install.sh | bash
```

#### 📦 **O que o instalador faz:**
- ✅ **Python 3.12+** (se não tiver)
- ✅ **MPV Player** (reprodução de vídeos)
- ✅ **yt-dlp** (extração de streaming)
- ✅ **Chrome/Chromium** (navegador para scraping)
- ✅ **Comando `hypr`** global

### macOS

#### 🍎 **Instalação Automática**

[![Download macOS](https://img.shields.io/badge/Download-macOS-000000?style=for-the-badge&logo=apple&logoColor=white)](https://raw.githubusercontent.com/inotyu/hypr/main/install.sh)

```bash
curl -fsSL https://raw.githubusercontent.com/inotyu/hypr/main/install.sh | bash
```

#### 📦 **O que o instalador faz:**
- ✅ **Python 3.12+** (se não tiver)
- ✅ **MPV Player** (reprodução de vídeos)
- ✅ **yt-dlp** (extração de streaming)
- ✅ **Chrome** (navegador para scraping)
- ✅ **Comando `hypr`** global

### Windows

#### 🚀 **Instalação Automática (Recomendado)**

[![Download Windows](https://img.shields.io/badge/Download-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://raw.githubusercontent.com/inotyu/hypr/main/install.bat)

**Clique no botão acima** ou execute manualmente:

```powershell
# Abra o PowerShell como Administrador e execute:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
irm https://raw.githubusercontent.com/inotyu/hypr/main/install.bat | iex
```

#### 📦 **O que o instalador faz:**
- ✅ **Python 3.12+** (se não tiver)
- ✅ **Git** (para atualizações)
- ✅ **Chrome** (navegador para scraping)
- ✅ **MPV Player** (reprodução de vídeos)
- ✅ **yt-dlp** (extração de streaming)
- ✅ **Atalho Desktop** (com logo oficial)
- ✅ **Script hypr.bat** (comando global)

#### 🎯 **Resultado:**
- 🖱️ **Atalho no desktop** com logo personalizada
- ⌨️ **Comando `hypr`** disponível globalmente
- 🎬 **Reprodução automática** no MPV
- 🎨 **Interface pronta** para uso

---

## 📖 Como Usar

```bash
# Buscar anime específico
hypr naruto

# Modo interativo completo
hypr -i

# Listar resultados sem interface
hypr -f one piece
```

**Controles da Interface:**

| Tecla | Função |
|-------|--------|
| `↑` `↓` ou `W` `S` | Navegação vertical |
| `Enter` | Selecionar item |
| `Q` | Sair da aplicação |

---

## 🗺️ Roadmap

- [ ] 📥 Sistema de download de episódios
- [ ] 🎨 Seletor de qualidade de vídeo (480p, 720p, 1080p)
- [ ] 🪟 Melhorias na experiência Windows
- [ ] 📚 Histórico de reprodução
- [ ] 🌙 Temas customizáveis
- [ ] 🔖 Sistema de marcadores
- [ ] 🔔 Notificações de novos episódios
- [ ] 🌐 Suporte multi-idioma
- [ ] 📱 Versão mobile

---

## 🤝 Contribuir

Contribuições são bem-vindas. Para contribuir:

1. Faça fork do repositório
2. Crie uma branch (`git checkout -b feature/nome-feature`)
3. Commit suas alterações (`git commit -m 'Adiciona: nova feature'`)
4. Push para a branch (`git push origin feature/nome-feature`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está licenciado sob a MIT License - consulte o arquivo [LICENSE](LICENSE) para detalhes.

---

## 💬 Suporte

- 🐞 [Reportar Issues](https://github.com/inotyu/hypr/issues)
- 💬 [Discussões](https://github.com/inotyu/hypr/discussions)
- 📖 [Documentação](https://github.com/inotyu/hypr/wiki)

---

<div align="center">

Desenvolvido por [inotyu](https://github.com/inotyu)

</div>
