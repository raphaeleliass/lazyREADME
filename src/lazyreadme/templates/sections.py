"""Templates para as seções do README."""

from typing import Dict


def get_sections(lang: str = "pt") -> Dict[str, str]:
    """Retorna as seções disponíveis no idioma especificado."""
    if lang == "pt":
        return {
            "1": "📝 Título e Descrição",
            "2": "🔧 Pré-requisitos e Instalação",
            "3": "📚 Uso e Exemplos",
            "4": "📖 Documentação",
            "5": "🤝 Como Contribuir",
            "6": "⚖️  Licença",
            "7": "🌟 Créditos",
            "8": "📫 Contato",
        }
    return {
        "1": "📝 Title and Description",
        "2": "🔧 Prerequisites and Installation",
        "3": "📚 Usage and Examples",
        "4": "📖 Documentation",
        "5": "🤝 How to Contribute",
        "6": "⚖️  License",
        "7": "🌟 Credits",
        "8": "📫 Contact",
    }


def get_section_content(section: str, lang: str) -> str:
    """Retorna o conteúdo de uma seção específica no idioma especificado."""
    pt_instructions = {
        "📝 Título e Descrição": '<div align="center" style="margin-top: 7rem">\n\n# Nome do Projeto\n\n<div style="margin-top: 1.5rem">\n\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n[![Stars](https://img.shields.io/github/stars/seu-usuario/seu-repositorio?style=social)](https://github.com/seu-usuario/seu-repositorio/stargazers)\n\n</div>\n\n<em align="center" style="width:80%; margin:0 auto; font-size:1.2em; color:#666">\nDescreva seu projeto aqui. O que ele faz? Por que é útil?\n</em>\n\n\n\n</div>\n\n<br>\n<br>\n<br>\n<br>\n',
        "🔧 Pré-requisitos e Instalação": "\n# **🔧 Pré-requisitos e Instalação**\n\n<br>\n\n### 📋 Prerequisites\n\n- Item 1\n- Item 2\n\n<br>\n\n### ⚡ Instalação\n\n#### 1. Clone o repositório:\n\n```bash\ngit clone seu-repositorio\n```\n\n#### 2. Navegue até o diretório:\n\n```bash\ncd seu-projeto\n```\n\n#### 3. Instale as dependências:\n\n```bash\npip install -r requirements.txt\n```\n\n<br>\n\n> 🎉 **Parabéns!** Você está pronto para começar.\n\n<br>\n\n---\n\n<br>\n<br>\n<br>\n<br>\n",
        "📚 Uso e Exemplos": "\n# **📚 Uso e Exemplos**\n\n<br>\n\n### 💡 Executando o Projeto\n\nExecute o script para iniciar:\n\n```bash\npython app.py\n```\n\n<br>\n\n### ✨ Exemplos\n\nAdicione exemplos de uso aqui:\n\n```bash\npython app.py --config config.json\n```\n\n<br>\n\n---\n\n<br>\n<br>\n<br>\n<br>\n",
        "📖 Documentação": "\n# **📖 Documentação**\n\n<br>\n\n### 🌟 Key Features\n\n- Feature 1\n- Feature 2\n- Feature 3\n\n<br>\n\n### 📚 External Documentation\n\n> [**🔧 Documentação Oficial**](link-da-documentacao)\n\n<br>\n\n---\n\n<br>\n<br>\n<br>\n<br>\n",
        "🤝 Como Contribuir": '\n# **🤝 Como Contribuir**\n\n<br>\n\n### 📝 Processo de Contribuição\n\n1. Fork o repositório\n\n2. Crie uma nova branch:\n\n   ```bash\n   git checkout -b feature-name\n   ```\n\n3. Commit suas mudanças:\n\n   ```bash\n   git commit -m "Add new feature"\n   ```\n\n4. Push para a branch:\n\n   ```bash\n   git push origin feature-name\n   ```\n\n5. Envie um pull request\n\n<br>\n\n### 📋 **Commit Guidelines**\n\n> Siga as mensagens de commit semânticas:\n\n- **feat:** Nova feature\n- **fix:** Correção de bug\n- **docs:** Mudanças na documentação\n\n<br>\n\n---\n\n<br>\n<br>\n<br>\n<br>\n',
        "⚖️  Licença": "\n# **⚖️  Licença**\n\n<br>\n\nEste projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.\n\n<br>\n\n---\n\n<br>\n<br>\n<br>\n<br>\n",
        "🌟 Créditos": "\n# **🌟 Créditos**\n\n<br>\n\n### 👥 Autores\n\n- 👤 [Seu Nome]\n\n<br>\n\n### 🛠️ Tecnologias\n\n- 🌐 Bibliotecas ou frameworks usados:\n  - Item 1\n  - Item 2\n\n<br>\n\n---\n\n<br>\n<br>\n<br>\n<br>\n",
        "📫 Contato": "\n# **📫 Contato**\n\n<br>\n\n### 📧 Para dúvidas ou suporte, entre em contato via:\n\n- 📨 Email: seu.email@exemplo.com\n\n- 📊 GitHub Issues: [Issues Page](link-para-issues)\n\n<br>\n\n---\n\n<br>\n<br>\n<br>\n<br>\n",
    }

    en_instructions = {
        "📝 Title and Description": '<div align="center" style="margin-top: 7rem">\n\n# Project Name\n\n<div style="margin-top: 1.5rem">\n\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n[![Stars](https://img.shields.io/github/stars/your-username/your-repository?style=social)](https://github.com/your-username/your-repository/stargazers)\n\n</div>\n\n<em align="center" style="width:80%; margin:0 auto; font-size:1.2em; color:#666">\nDescribe your project here. What does it do? Why is it useful?\n</em>\n\n\n\n</div>\n\n<br>\n<br>\n<br>\n<br>\n',
        "🔧 Prerequisites and Installation": "\n# **🔧 Prerequisites and Installation**\n\n<br>\n\n### 📋 Prerequisites\n\n- Item 1\n- Item 2\n\n<br>\n\n### ⚡ Installation\n\n#### 1. Clone the repository:\n\n```bash\ngit clone your-repository\n```\n\n#### 2. Navigate to directory:\n\n```bash\ncd your-project\n```\n\n#### 3. Install dependencies:\n\n```bash\npip install -r requirements.txt\n```\n\n<br>\n\n> 🎉 **Congratulations!** You're all set.\n\n<br>\n\n---\n\n<br>\n<br>\n<br>\n<br>\n",
        "📚 Usage and Examples": "\n# **📚 Usage and Examples**\n\n<br>\n\n### 💡 Running the Project\n\nRun the script to start:\n\n```bash\npython app.py\n```\n\n<br>\n\n### ✨ Examples\n\nAdd usage examples here:\n\n```bash\npython app.py --config config.json\n```\n\n<br>\n\n---\n\n<br>\n<br>\n<br>\n<br>\n",
        "📖 Documentation": "\n# **📖 Documentation**\n\n<br>\n\n### 🌟 Key Features\n\n- Feature 1\n- Feature 2\n- Feature 3\n\n<br>\n\n### 📚 External Documentation\n\n> [**🔧 Official Documentation**](documentation-link)\n\n<br>\n\n---\n\n<br>\n<br>\n<br>\n<br>\n",
        "🤝 How to Contribute": '\n# **🤝 How to Contribute**\n\n<br>\n\n### 📝 Contribution Process\n\n1. Fork the repository\n\n2. Create a new branch:\n\n   ```bash\n   git checkout -b feature-name\n   ```\n\n3. Commit your changes:\n\n   ```bash\n   git commit -m "Add new feature"\n   ```\n\n4. Push the branch:\n\n   ```bash\n   git push origin feature-name\n   ```\n\n5. Submit a pull request\n\n<br>\n\n### 📋 **Commit Guidelines**\n\n> Follow semantic commit messages:\n\n- **feat:** New feature\n- **fix:** Bug fix\n- **docs:** Documentation changes\n\n<br>\n\n---\n\n<br>\n<br>\n<br>\n<br>\n',
        "⚖️  License": "\n# **⚖️  License**\n\n<br>\n\nThis project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.\n\n<br>\n\n---\n\n<br>\n<br>\n<br>\n<br>\n",
        "🌟 Credits": "\n# **🌟 Credits**\n\n<br>\n\n### 👥 Authors\n\n- 👤 [Your Name]\n\n<br>\n\n### 🛠️ Technologies\n\n- 🌐 Libraries or frameworks used:\n  - Item 1\n  - Item 2\n\n<br>\n\n---\n\n<br>\n<br>\n<br>\n<br>\n",
        "📫 Contact": "\n# **📫 Contact**\n\n<br>\n\n### 📧 For questions or support, reach out via:\n\n- 📨 Email: your.email@example.com\n\n- 📊 GitHub Issues: [Issues Page](issues-link)\n\n<br>\n\n---\n\n<br>\n<br>\n<br>\n<br>\n",
    }

    return en_instructions.get(section, "") if lang == "en" else pt_instructions.get(section, "")
