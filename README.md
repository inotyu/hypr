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

```bash
curl -fsSL https://raw.githubusercontent.com/inotyu/hypr/main/install.sh | bash
```

### macOS

```bash
curl -fsSL https://raw.githubusercontent.com/inotyu/hypr/main/install.sh | bash
```

### Windows

Abra o **PowerShell como Administrador**:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
irm https://raw.githubusercontent.com/inotyu/hypr/main/install.ps1 | iex
```

Reinicie o terminal após a instalação para carregar as variáveis de ambiente.

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
