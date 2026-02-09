# 📚 Guia: Como Subir o Hypr para o GitHub

## 🚀 Passo 1: Preparar o Projeto

### 1.1 Limpar arquivos desnecessários
```bash
# Remover arquivos temporários
rm -rf __pycache__/
rm -rf */__pycache__/
rm -rf *.pyc
rm -rf .pytest_cache/
```

### 1.2 Verificar estrutura final
```bash
tree -I '__pycache__|*.pyc' .
```

Deve ficar assim:
```
.
├── README.md
├── install.sh
├── .gitignore
└── hypr_scraper/
    ├── hypr
    └── src/
        ├── cli/
        │   ├── interactive.py
        │   └── selector.py
        └── scraper/
            └── hypr_scraper.py
```

## 🔧 Passo 2: Criar Repositório no GitHub

### 2.1 Acesse https://github.com
- Clique em **"New repository"**
- **Nome**: `hypr` ou `hypr-anime-scraper`
- **Descrição**: "🎬 O melhor scraper de animes para terminal!"
- **Visibilidade**: Pública
- ✅ **Add a README file** (desmarcar - já temos)
- ✅ **Add .gitignore** (desmarcar - já temos)
- Clique em **"Create repository"**

## 💻 Passo 3: Configurar Git Local

### 3.1 Inicializar repositório
```bash
cd /caminho/para/seu/projeto
git init
```

### 3.2 Configurar usuário (se ainda não fez)
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

### 3.3 Adicionar arquivos
```bash
git add .
```

### 3.4 Primeiro commit
```bash
git commit -m "🎬 Initial commit: Hypr Anime Scraper

✨ Features:
- Busca de animes em animesdigital.org
- Interface interativa com curses
- Reprodução automática no MPV
- Instalação automática universal
- Cross-platform (Linux/macOS/Windows)

📦 Includes:
- Script de instalação completa
- README profissional
- Estrutura modular organizada"
```

## 🔗 Passo 4: Conectar ao GitHub

### 4.1 Adicionar remote
```bash
# Substitua SEU_USERNAME pelo seu usuário do GitHub
git remote add origin https://github.com/SEU_USERNAME/hypr.git
```

### 4.2 Fazer push
```bash
git branch -M main
git push -u origin main
```

## 🎨 Passo 5: Personalizar o Repositório

### 5.1 Adicionar tópicos
No GitHub, vá em **Settings > General > Topics** e adicione:
- `anime`
- `scraper`
- `python`
- `terminal`
- `cli`
- `selenium`
- `mpv`

### 5.2 Adicionar badges no README
Atualize o README.md para incluir badges:

```markdown
# Hypr - Anime Scraper

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)]()
[![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)]()
```

### 5.3 Adicionar license
Crie um arquivo `LICENSE`:

```
MIT License

Copyright (c) 2024 SEU_USERNAME

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🔄 Passo 6: Manter Atualizado

### 6.1 Para futuras atualizações
```bash
# Fazer mudanças
git add .
git commit -m "✨ Nova feature: descrição"
git push
```

### 6.2 Releases
- Vá em **Releases** no GitHub
- Clique **"Create a new release"**
- **Tag**: `v1.0.0`
- **Title**: `Hypr v1.0.0 - Lançamento inicial`
- **Description**: Descreva as funcionalidades

## 📊 Passo 7: Otimizar para Descoberta

### 7.1 SEO do repositório
- **Descrição**: "🎬 O melhor scraper de animes para terminal! Busque, selecione e assista seus animes favoritos diretamente no terminal."
- **Website**: Deixe vazio ou adicione um site futuro
- **Tópicos**: anime, scraper, python, terminal, cli, selenium, mpv

### 7.2 README otimizado
Já criamos um README profissional com:
- ✅ Emojis para atrair atenção
- ✅ Badges informativos
- ✅ Instalação simples
- ✅ Exemplos de uso
- ✅ Funcionalidades destacadas

## 🎯 Resultado Final

Seu repositório estará assim:
- 📁 **Estrutura limpa** e organizada
- 📖 **README profissional** com tudo explicado
- 🔒 **.gitignore** completo
- 📦 **Script de instalação** automático
- ⭐ **Pronto para receber stars** e contribuições

## 🚀 Próximos Passos

1. **Divulgar**: Poste no Reddit (r/Python, r/anime), Discord, etc.
2. **Documentação**: Crie wiki no GitHub para tutoriais avançados
3. **Issues**: Configure templates para bugs e features
4. **CI/CD**: Adicione GitHub Actions para testes automáticos

**Seu projeto Hypr estará no GitHub profissionalmente!** 🎉
