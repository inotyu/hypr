<div align="center">

<img src="hypr_scraper/src/file_00000000996871f59d54ec96a1919c08.png" alt="HyprOnline" width="600"/>

# HyprOnline

### A forma mais elegante de assistir animes no terminal

Transforme seu terminal em um centro de streaming completo. Busque entre milhares de títulos, navegue com interface minimalista e assista com qualidade premium - tudo isso sem sair da linha de comando.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey.svg?style=for-the-badge)](https://github.com/inotyu/hypr)

<p align="center">
  <a href="#-instalação">Instalação</a> •
  <a href="#-como-usar">Como Usar</a> •
  <a href="#-funcionalidades">Funcionalidades</a> •
  <a href="#-roadmap">Roadmap</a> •
  <a href="#-contribuir">Contribuir</a>
</p>

</div>

---

## 🌟 Funcionalidades

O HyprOnline foi construído com uma filosofia clara: simplicidade extrema combinada com poder absoluto. Cada feature foi pensada para eliminar friction entre você e o conteúdo que quer assistir.

<table>
<tr>
<td width="50%" valign="top">

### 🔍 Busca Inteligente

O sistema de busca usa algoritmos fuzzy que entendem erros de digitação, abreviações e nomes parciais. Digite "narot" e ele encontra "Naruto". Digite "one piec" e ele encontra "One Piece". O motor de busca aprende padrões comuns e melhora com o uso.

Suporta busca por:
- Nome do anime (completo ou parcial)
- Nome alternativo (inglês, japonês)
- Gênero e tags
- Temporada e ano

### 🎯 Interface Interativa

A interface usa curses/ncurses para criar uma experiência fluida diretamente no terminal. Navegação com setas ou WASD, feedback visual em tempo real, e design responsivo que se adapta perfeitamente ao tamanho da sua janela.

Características:
- Design minimalista e limpo
- Navegação por teclado otimizada
- Indicadores visuais claros
- Sem lag ou travamentos
- Tema escuro por padrão

### 🎬 Reprodução Premium

Prioriza o MPV player, conhecido por ser o melhor reprodutor de vídeo open-source disponível. Oferece qualidade de imagem superior, baixíssimo uso de CPU e suporte para praticamente qualquer codec. Se o MPV não estiver disponível, faz fallback automático para o navegador.

Vantagens do MPV:
- Qualidade de vídeo excepcional
- Controles avançados via teclado
- Baixo consumo de recursos
- Suporte para legendas avançado

</td>
<td width="50%" valign="top">

### ⚡ Performance Brutal

O scraper foi otimizado para velocidade máxima. Usa cache inteligente que memoriza suas buscas recentes, elimina requisições redundantes e faz scraping assíncrono quando possível. A maioria das operações completa em menos de 100ms.

Otimizações incluem:
- Cache local de resultados
- Scraping assíncrono paralelo
- Compressão automática de dados
- Reuso de conexões HTTP
- Pré-carregamento inteligente

### 🖥️ Verdadeiro Cross-Platform

Funciona identicamente em Linux, macOS e Windows. Os scripts de instalação detectam automaticamente seu sistema operacional e instalam as dependências corretas. Zero configuração manual necessária.

Suporte completo para:
- Linux (Ubuntu, Debian, Fedora, Arch)
- macOS (Intel e Apple Silicon)
- Windows 10/11 (PowerShell)
- WSL (Windows Subsystem for Linux)

### 🎨 Experiência Limpa

Nada de anúncios invasivos. Nada de popups irritantes. Nada de trackers escondidos. Apenas você, o terminal, e o anime que escolheu assistir. A experiência é tão minimalista quanto poderosa.

Filosofia zero-bloat:
- Interface sem distrações
- Sem coleta de dados
- Sem telemetria
- Código aberto e auditável

</td>
</tr>
</table>

---

## 🚀 Instalação

A instalação é completamente automática. O script detecta seu sistema operacional, instala todas as dependências necessárias e configura o ambiente para você. Leva cerca de 2-3 minutos.

### 🐧 Linux

```bash
curl -fsSL https://raw.githubusercontent.com/inotyu/hypr/main/install.sh | bash
```

**O que será instalado:**
- Python 3.11 ou superior (se não estiver presente)
- Google Chrome (necessário para o scraping funcionar)
- MPV Player (o melhor reprodutor de vídeo)
- Bibliotecas Python: selenium, webdriver-manager, yt-dlp, requests
- Configuração automática de PATH e aliases

**Distribuições testadas:**
- Ubuntu 20.04, 22.04, 24.04
- Debian 11, 12
- Fedora 38, 39, 40
- Arch Linux (btw)
- Pop!_OS, Linux Mint, Elementary

### 🍎 macOS

```bash
curl -fsSL https://raw.githubusercontent.com/inotyu/hypr/main/install.sh | bash
```

**O que será instalado:**
- Python 3.11+ via Homebrew (caso necessário)
- Google Chrome (se ainda não instalado)
- MPV Player via Homebrew
- Bibliotecas Python otimizadas para macOS
- Configuração de PATH no .zshrc ou .bash_profile

**Compatibilidade:**
- macOS Monterey (12.x)
- macOS Ventura (13.x)
- macOS Sonoma (14.x)
- macOS Sequoia (15.x)
- Suporte para Intel e Apple Silicon (M1/M2/M3)

### 🪟 Windows

Abra o **PowerShell como Administrador** e execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
irm https://raw.githubusercontent.com/inotyu/hypr/main/install.ps1 | iex
```

**O que será instalado:**
- Python 3.11+ (download automático se necessário)
- Google Chrome (via instalador oficial)
- MPV Player (via Chocolatey ou download direto)
- windows-curses (necessário para a interface funcionar)
- Todas as bibliotecas Python necessárias
- Configuração de PATH no sistema

**Requisitos:**
- Windows 10 (build 1809 ou superior)
- Windows 11
- PowerShell 5.1 ou superior
- Conexão com internet

**Após a instalação em qualquer plataforma:** Feche e abra o terminal novamente para que o comando `hypr` seja reconhecido. Você saberá que funcionou quando digitar `hypr --version` e ver a versão instalada.

---

## 📖 Como Usar

### Comandos Principais

O HyprOnline possui três modos de operação, cada um otimizado para um caso de uso específico:

```bash
# Modo padrão: busca direta
hypr attack on titan

# Modo interativo: exploração completa
hypr -i

# Modo lista: output para scripts
hypr -f demon slayer
```

**Modo Padrão (Busca Direta):**
Este é o modo mais rápido. Digite o nome do anime e ele já mostra os resultados. Você navega, escolhe o episódio, e assiste. Simples assim.

```bash
hypr naruto
hypr "one piece"
hypr steins gate
```

**Modo Interativo (`-i`):**
Perfeito quando você quer explorar sem pressa. Mostra uma interface completa onde você pode navegar por categorias, ver detalhes dos animes, e descobrir novos títulos.

```bash
hypr -i
```

**Modo Lista (`-f`):**
Retorna resultados em formato de lista pura, sem interface interativa. Útil para integrar com outros comandos ou scripts de automação.

```bash
hypr -f jujutsu kaisen
hypr -f cowboy bebop | grep "Episódio"
```

### ⌨️ Controles da Interface

A navegação foi projetada para ser intuitiva tanto para usuários de vim quanto para iniciantes:

<div align="center">

| Ação | Teclas Principais | Alternativas |
|:-----|:------------------|:-------------|
| **Navegar para cima** | `↑` | `W` ou `K` |
| **Navegar para baixo** | `↓` | `S` ou `J` |
| **Selecionar item** | `Enter` | `Space` |
| **Voltar/Cancelar** | `Q` | `Esc` |
| **Buscar** | `/` | `Ctrl+F` |
| **Ajuda** | `?` | `H` |

</div>

### Fluxo de Trabalho Típico

Veja como é simples assistir um anime do início ao fim:

**1. Busque o anime:**
```bash
$ hypr jujutsu kaisen
```

**2. O sistema faz a busca e mostra os resultados:**
```
🔍 Buscando "jujutsu kaisen"...
⚡ Scraping de 3 fontes...
✅ 15 resultados encontrados em 0.8s

╔════════════════════════════════════════════╗
║  1. Jujutsu Kaisen (2020)                  ║
║     → 24 episódios | Ação, Sobrenatural    ║
║                                            ║
║  2. Jujutsu Kaisen 2ª Temporada (2023)     ║
║     → 23 episódios | Ação, Sobrenatural    ║
║                                            ║
║  3. Jujutsu Kaisen 0 (Filme - 2021)        ║
║     → Filme | Ação, Sobrenatural           ║
╚════════════════════════════════════════════╝

Use ↑↓ para navegar | Enter para selecionar | Q para sair
```

**3. Navegue com as setas e pressione Enter no anime desejado**

**4. Escolha o episódio:**
```
╔════════════════════════════════════════════╗
║  Jujutsu Kaisen (2020)                     ║
║  Selecione o episódio:                     ║
║                                            ║
║  → Episódio 01 - Ryomen Sukuna             ║
║    Episódio 02 - Para Você, Algum Dia      ║
║    Episódio 03 - Garota de Aço             ║
║    Episódio 04 - Útero Amaldiçoado         ║
║    ...                                     ║
╚════════════════════════════════════════════╝
```

**5. O vídeo abre automaticamente no MPV ou navegador**

Todo o processo, da busca à reprodução, leva menos de 10 segundos.

### Exemplos Práticos

**Assistir um episódio específico rapidamente:**
```bash
hypr "attack on titan"
# Navegue até o episódio desejado e assista
```

**Descobrir novos animes:**
```bash
hypr -i
# Explore as categorias e rankings
```

**Maratona de fim de semana:**
```bash
hypr "death note"
# Assista um episódio após o outro
```

**Integração com outros comandos (usuários avançados):**
```bash
# Listar todos os episódios disponíveis
hypr -f "demon slayer" | grep "Episódio"

# Buscar e salvar a lista
hypr -f "naruto" > minha_lista.txt
```

---

## 🔮 Roadmap

O desenvolvimento do HyprOnline segue uma roadmap clara focada em adicionar features que realmente importam para os usuários. Cada item abaixo foi cuidadosamente planejado baseado em feedback da comunidade.

### 🚧 Em Desenvolvimento Ativo

Estas features estão sendo desenvolvidas agora e devem chegar nas próximas versões:

**📥 Sistema de Download Completo**
- Baixar episódios individuais ou temporadas completas
- Downloads em segundo plano com gerenciador visual
- Organização automática em pastas por anime/temporada
- Suporte para downloads paralelos (múltiplos episódios simultaneamente)
- Retomada automática de downloads interrompidos
- Conversão automática para formatos compatíveis
- Sistema de fila de downloads com prioridades

**🎨 Seletor de Qualidade Avançado**
- Escolha manual entre 480p, 720p, 1080p, 4K
- Detecção automática da melhor qualidade disponível
- Priorização baseada na velocidade da internet
- Opção de forçar qualidade específica
- Preview de qualidade antes de carregar
- Indicador de tamanho estimado por qualidade
- Modo "auto" que aprende suas preferências

**🪟 Suporte Windows de Primeira Classe**
- Instalador `.exe` standalone (sem precisar de PowerShell)
- Interface GUI opcional para usuários não-técnicos
- Integração nativa com Windows Terminal
- Atalhos de teclado do Windows
- Notificações do sistema Windows 10/11
- Context menu no Explorer (botão direito > "Assistir com Hypr")

**📚 Sistema de Histórico e Progresso**
- Rastreamento automático de episódios assistidos
- "Continue assistindo" na tela inicial
- Sincronização de progresso entre dispositivos (opcional)
- Estatísticas detalhadas (tempo assistido, animes completos, etc)
- Backup e restauração de histórico
- Exportação de histórico para MAL/AniList

### 📋 Planejado para Futuro Próximo

Features que estão no pipeline e serão desenvolvidas após as features atuais:

**🌙 Sistema de Temas Completo**
- Dark mode e Light mode built-in
- Editor de temas visual
- Temas da comunidade (compartilháveis)
- Suporte para cores RGB customizadas
- Temas por horário (automático dark/light)
- Galeria de temas pré-prontos

**🔖 Sistema de Listas e Favoritos**
- Múltiplas listas customizadas
- Tags e categorias personalizadas
- Avaliações e notas pessoais
- Compartilhamento de listas públicas
- Importação de listas do MAL/AniList
- Recomendações baseadas nos seus favoritos

**🔔 Sistema de Notificações Inteligente**
- Alertas de novos episódios dos seus animes
- Notificações desktop nativas
- Opção de notificações por email
- Integração com Telegram/Discord (webhook)
- Agendamento de lembretes personalizados
- Modo "não perturbe" configurável

**🌐 Suporte Multi-idioma Completo**
- Interface em PT-BR, EN, ES, JP
- Legendas em múltiplos idiomas
- Seleção automática baseada na região
- Dual audio quando disponível
- Sincronização de legendas ajustável
- Suporte para legendas .srt/.ass externas

**📱 Aplicativo Mobile Nativo**
- Apps nativos para Android e iOS
- Sincronização completa com versão desktop
- Modo offline com downloads
- Player otimizado para mobile
- Controles touch intuitivos
- Chromecast e AirPlay support

### 💡 Ideias Futuras (Long-term)

Recursos mais ambiciosos planejados para versões futuras:

**🤖 Recomendações por IA**
- Sistema de recomendação baseado em machine learning
- Análise de padrões de visualização
- Descoberta de animes similares aos seus favoritos
- "Se você gostou de X, vai gostar de Y"

**🎮 Integração com Plataformas**
- Sincronização com MyAnimeList
- Integração com AniList
- Conexão com Crunchyroll/Funimation (para quem tem conta)
- API pública para desenvolvedores

**📊 Estatísticas Avançadas**
- Dashboard com gráficos de uso
- Heatmap de horários de visualização
- Top 10 animes mais assistidos
- Análise de gêneros preferidos
- Tempo total assistido

**🔌 Sistema de Plugins**
- Suporte para plugins da comunidade
- API de extensão documentada
- Loja de plugins integrada
- Hot reload de plugins

### 🎯 Como Contribuir com o Roadmap

Tem uma ideia que não está listada? Quer votar nas features que mais importam para você?

- **📢 Sugira features:** Abra uma [issue com tag "feature-request"](https://github.com/inotyu/hypr/issues/new)
- **🗳️ Vote em features:** Reaja com 👍 nas issues existentes
- **💬 Discuta ideias:** Participe nas [Discussions](https://github.com/inotyu/hypr/discussions)
- **🔨 Contribua código:** Implemente features do roadmap e abra um PR

---

## 🤝 Contribuir

O HyprOnline é um projeto open-source e prospera com contribuições da comunidade. Seja você um desenvolvedor experiente ou alguém fazendo seu primeiro PR, sua contribuição é valiosa!

### 🌟 Formas de Contribuir

**Para Desenvolvedores:**
- 🐛 Corrigir bugs conhecidos
- ✨ Implementar features do roadmap
- ⚡ Melhorar performance
- 🧪 Adicionar testes
- 📝 Melhorar documentação
- 🌍 Adicionar traduções

**Para Não-Desenvolvedores:**
- 📢 Reportar bugs com detalhes
- 💡 Sugerir melhorias
- 📖 Melhorar a documentação
- 🎨 Criar temas visuais
- 🌍 Traduzir o projeto
- ⭐ Dar estrela no projeto

### 🔧 Setup para Desenvolvimento

Se você quer contribuir com código, siga estes passos:

**1. Fork e Clone:**
```bash
git clone https://github.com/SEU-USUARIO/hypr.git
cd hypr
```

**2. Configure o ambiente:**
```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**3. Teste se está funcionando:**
```bash
# Linux/macOS
python3 hypr_scraper/hypr --version

# Windows
python hypr_scraper/hypr --version
```

**4. Crie uma branch para sua feature:**
```bash
git checkout -b feature/minha-feature-incrivel
```

**5. Faça suas alterações e teste bem**

**6. Commit com mensagens claras:**
```bash
git commit -m "✨ Add: Sistema de favoritos"
git commit -m "🐛 Fix: Crash ao buscar anime com caracteres especiais"
git commit -m "📝 Docs: Adiciona exemplos de uso avançado"
```

**7. Push e abra um Pull Request:**
```bash
git push origin feature/minha-feature-incrivel
```

### 📋 Convenções de Código

Para manter o código consistente, seguimos estas convenções:

**Python:**
- Siga PEP 8
- Use type hints quando possível
- Docstrings em funções públicas
- Máximo 100 caracteres por linha

**Commits:**
- Use emojis no início: ✨ (feature), 🐛 (bugfix), 📝 (docs), ⚡ (performance)
- Mensagens em português ou inglês
- Seja descritivo mas conciso

**Pull Requests:**
- Descreva o que mudou e por quê
- Adicione screenshots se for mudança visual
- Referencie issues relacionadas
- Aguarde review antes de fazer merge

### 🎯 Boas Primeiras Contribuições

Procurando por onde começar? Veja issues marcadas com:
- `good-first-issue` - Perfeitas para iniciantes
- `help-wanted` - Precisamos de ajuda aqui
- `documentation` - Melhorias na documentação

---

## 📜 Licença

Este projeto é distribuído sob a licença MIT. Isso significa que você pode:

✅ Usar comercialmente  
✅ Modificar como quiser  
✅ Distribuir livremente  
✅ Usar em projetos privados  

**Única condição:** Manter o aviso de copyright e licença nos arquivos.

Veja o arquivo [LICENSE](LICENSE) para o texto completo da licença.

---

## 💬 Suporte e Comunidade

Precisa de ajuda? Encontrou um bug? Quer bater um papo sobre anime? Temos vários canais:

<div align="center">

[![GitHub Issues](https://img.shields.io/badge/Issues-Reporte%20Bugs-red?style=for-the-badge&logo=github)](https://github.com/inotyu/hypr/issues)
[![GitHub Discussions](https://img.shields.io/badge/Discussions-Comunidade-blue?style=for-the-badge&logo=github)](https://github.com/inotyu/hypr/discussions)
[![Wiki](https://img.shields.io/badge/Wiki-Documentação-green?style=for-the-badge&logo=wikipedia)](https://github.com/inotyu/hypr/wiki)

</div>

### 📬 Canais de Suporte

**🐞 Para Bugs:**
Encontrou algo que não funciona? [Abra uma issue](https://github.com/inotyu/hypr/issues/new) com:
- Descrição clara do problema
- Passos para reproduzir
- Versão do HyprOnline (`hypr --version`)
- Sistema operacional e versão
- Screenshots se aplicável

**💬 Para Discussões Gerais:**
Quer conversar sobre o projeto? [Discussions](https://github.com/inotyu/hypr/discussions) é o lugar certo para:
- Tirar dúvidas
- Compartilhar casos de uso
- Sugerir melhorias
- Mostrar seus scripts customizados

**📖 Para Documentação:**
Procurando por guias detalhados? Confira nossa [Wiki](https://github.com/inotyu/hypr/wiki) com:
- Guias de instalação detalhados
- Troubleshooting comum
- Tutoriais avançados
- FAQ completo

**💼 Para Questões Privadas:**
Contato direto por email para:
- Parcerias
- Questões de segurança
- Propostas comerciais

---

## 🏆 Créditos

**Desenvolvido por:** [inotyu](https://github.com/inotyu)

**Contribuidores:** Obrigado a todos que contribuíram com código, sugestões e bug reports!

**Tecnologias Utilizadas:**
- Python 3.11+
- Selenium (web scraping)
- yt-dlp (extração de vídeo)
- MPV (reprodução)
- curses (interface)

**Inspirações:**
- ani-cli
- mpv
- yt-dlp

---

<div align="center">

### ⭐ Se este projeto facilitou sua vida, deixe uma estrela!

Cada estrela nos motiva a continuar melhorando o HyprOnline.

**Feito com ❤️ e muito café por [inotyu](https://github.com/inotyu)**

*"A melhor forma de assistir anime é do jeito que você quiser"*

<sub>HyprOnline • 2024-2026 • Licença MIT • Feito com Python 🐍</sub>

</div>
