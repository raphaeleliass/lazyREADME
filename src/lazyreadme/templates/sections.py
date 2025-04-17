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
            "6": "🌟 Créditos",
            "7": "📫 Contato",
            "8": "⚖️  Licença",
        }
    return {
        "1": "📝 Title and Description",
        "2": "🔧 Prerequisites and Installation",
        "3": "📚 Usage and Examples",
        "4": "📖 Documentation",
        "5": "🤝 How to Contribute",
        "6": "🌟 Credits",
        "7": "📫 Contact",
        "8": "⚖️  License",
    }


def get_section_content(section: str, lang: str) -> str:
    """Retorna o conteúdo de uma seção específica no idioma especificado."""
    pt_instructions = {
        "📝 Título e Descrição": '<div align="center">\n\n# Nome do Projeto\n\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n[![Stars](https://img.shields.io/github/stars/seu-usuario/seu-repositorio?style=social)](https://github.com/seu-usuario/seu-repositorio/stargazers)\n\n<em style="display: block; margin: 1rem auto; max-width: 600px; color: #666">\nDescreva seu projeto aqui. O que ele faz? Por que é útil?\n</em>\n\n</div>\n\n---\n',
        "🔧 Pré-requisitos e Instalação": '\n<p style="font-size: 1.6rem; margin-top: 4rem">🔧 Pré-requisitos</p>\n\n- Item 1\n- Item 2\n\n<p style="font-size: 1.6rem; margin-top: 4rem">⚙️ Instalação</p>\n\n```bash\n# Clone o repositório\ngit clone seu-repositorio\n\n# Navegue até o diretório\ncd seu-projeto\n\n# Instale as dependências\npip install -r requirements.txt\n```\n\n> 🎉 **Pronto para começar!**\n\n---\n',
        "📚 Uso e Exemplos": '\n<p style="font-size: 1.6rem; margin-top: 4rem">💡 Executando o Projeto</p>\n\n```bash\npython app.py\n```\n\n<p style="font-size: 1.6rem; margin-top: 4rem">✨ Exemplos de Uso</p>\n\n```bash\npython app.py --config config.json\n```\n\n---\n',
        "📖 Documentação": '\n<p style="font-size: 1.6rem; margin-top: 4rem">🌟 Principais Funcionalidades</p>\n\n- Feature 1\n- Feature 2\n- Feature 3\n\n<p style="font-size: 1.6rem; margin-top: 4rem">📚 Links Úteis</p>\n\n> [📚 Documentação Oficial](link-da-documentacao)\n\n---\n',
        "🤝 Como Contribuir": '\n<p style="font-size: 1.6rem; margin-top: 4rem">🔄 Processo de Contribuição</p>\n\n```bash\n# 1. Fork o repositório\n\n# 2. Crie uma nova branch\ngit checkout -b feature-name\n\n# 3. Commit suas mudanças\ngit commit -m "Add new feature"\n\n# 4. Push para a branch\ngit push origin feature-name\n\n# 5. Envie um pull request\n```\n\n<p style="font-size: 1.6rem; margin-top: 4rem">📋 Padrão de Commits</p>\n\n- `feat`: Nova feature\n- `fix`: Correção de bug\n- `docs`: Mudanças na documentação\n\n---\n',
        "🌟 Créditos": '\n<p style="font-size: 1.6rem; margin-top: 4rem">👥 Autores</p>\n\n👤 [Seu Nome]\n\n<p style="font-size: 1.6rem; margin-top: 4rem">🛠️ Tecnologias Utilizadas</p>\n\n- Item 1\n- Item 2\n\n---\n',
        "📫 Contato": '\n<p style="font-size: 1.6rem; margin-top: 4rem">📬 Para dúvidas ou suporte</p>\n\n📨 Email: seu.email@exemplo.com\n📊 [GitHub Issues](link-para-issues)\n\n---\n',
        "⚖️  Licença": "\nEste projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.\n\n---\n",
    }

    en_instructions = {
        "📝 Title and Description": '<div align="center">\n\n# Project Name\n\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n[![Stars](https://img.shields.io/github/stars/your-username/your-repository?style=social)](https://github.com/your-username/your-repository/stargazers)\n\n<em style="display: block; margin: 1rem auto; max-width: 600px; color: #666">\nDescribe your project here. What does it do? Why is it useful?\n</em>\n\n</div>\n\n---\n',
        "🔧 Prerequisites and Installation": '\n<p style="font-size: 1.6rem; margin-top: 4rem">🔧 Prerequisites</p>\n\n- Item 1\n- Item 2\n\n<p style="font-size: 1.6rem; margin-top: 4rem">⚙️ Installation</p>\n\n```bash\n# Clone the repository\ngit clone your-repository\n\n# Navigate to directory\ncd your-project\n\n# Install dependencies\npip install -r requirements.txt\n```\n\n> 🎉 **Ready to start!**\n\n---\n',
        "📚 Usage and Examples": '\n<p style="font-size: 1.6rem; margin-top: 4rem">💡 Running the Project</p>\n\n```bash\npython app.py\n```\n\n<p style="font-size: 1.6rem; margin-top: 4rem">✨ Usage Examples</p>\n\n```bash\npython app.py --config config.json\n```\n\n---\n',
        "📖 Documentation": '\n<p style="font-size: 1.6rem; margin-top: 4rem">🌟 Key Features</p>\n\n- Feature 1\n- Feature 2\n- Feature 3\n\n<p style="font-size: 1.6rem; margin-top: 4rem">📚 Useful Links</p>\n\n> [📚 Official Documentation](documentation-link)\n\n---\n',
        "🤝 How to Contribute": '\n<p style="font-size: 1.6rem; margin-top: 4rem">🔄 Contribution Process</p>\n\n```bash\n# 1. Fork the repository\n\n# 2. Create a new branch\ngit checkout -b feature-name\n\n# 3. Commit your changes\ngit commit -m "Add new feature"\n\n# 4. Push the branch\ngit push origin feature-name\n\n# 5. Submit a pull request\n```\n\n<p style="font-size: 1.6rem; margin-top: 4rem">📋 Commit Guidelines</p>\n\n- `feat`: New feature\n- `fix`: Bug fix\n- `docs`: Documentation changes\n\n---\n',
        "🌟 Credits": '\n<p style="font-size: 1.6rem; margin-top: 4rem">👥 Authors</p>\n\n👤 [Your Name]\n\n<p style="font-size: 1.6rem; margin-top: 4rem">🛠️ Technologies Used</p>\n\n- Item 1\n- Item 2\n\n---\n',
        "📫 Contact": '\n<p style="font-size: 1.6rem; margin-top: 4rem">📬 For questions or support</p>\n\n📨 Email: your.email@example.com\n📊 [GitHub Issues](issues-link)\n\n---\n',
        "⚖️  License": "\nThis project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.\n\n---\n",
    }

    return en_instructions.get(section, "") if lang == "en" else pt_instructions.get(section, "")
