"""Interface de linha de comando do lazyREADME."""

import os
import sys
from typing import List
from colorama import Fore
import questionary

from ..utils.console import clear_screen, print_header
from ..templates.sections import get_sections, get_section_content

def select_language() -> str:
    """Solicita ao usuário que escolha o idioma."""
    options = ["🇧🇷 Português", "🇺🇸 English"]

    print(f"\n{Fore.CYAN}🌐 Escolha o idioma do README:")

    choice = questionary.select(
        "Idioma:",
        choices=options,
    ).ask()

    if not choice:
        print(f"\n{Fore.RED}❌ Operação cancelada pelo usuário.")
        sys.exit(0)

    return "pt" if "Português" in choice else "en"

def select_sections(lang: str) -> List[str]:
    """Solicita ao usuário que selecione as seções desejadas."""
    sections = get_sections(lang)
    section_names = list(sections.values())

    if lang == "pt":
        print(f"{Fore.CYAN}📋 Selecione as seções que deseja incluir no README:")
        print(f"{Fore.YELLOW}↑↓ Use as setas para navegar")
        print(f"{Fore.YELLOW}[space] Para selecionar")
        print(f"{Fore.YELLOW}[enter] Para confirmar\n")
        error_msg = f"{Fore.RED}❌ Por favor, selecione pelo menos uma seção"
    else:
        print(f"{Fore.CYAN}📋 Select the sections to include in the README:")
        print(f"{Fore.YELLOW}↑↓ Use arrows to navigate")
        print(f"{Fore.YELLOW}[space] To select")
        print(f"{Fore.YELLOW}[enter] To confirm\n")
        error_msg = f"{Fore.RED}❌ Please select at least one section"

    choices = questionary.checkbox(
        "README Sections:" if lang == "en" else "Seções do README:",
        choices=section_names,
        validate=lambda x: len(x) > 0 or error_msg
    ).ask()

    if not choices:
        msg = "Operation cancelled by user" if lang == "en" else "Operação cancelada pelo usuário"
        print(f"\n{Fore.RED}❌ {msg}")
        sys.exit(0)

    return choices

def create_readme(sections: List[str], lang: str) -> None:
    """Cria o arquivo README.md com as seções selecionadas."""
    msg_generating = "Generating your README..." if lang == "en" else "Gerando seu README..."
    msg_adding = "Adding section" if lang == "en" else "Adicionando seção"
    msg_success = "README.md created successfully!" if lang == "en" else "README.md criado com sucesso!"
    msg_saved = "File saved as" if lang == "en" else "Arquivo salvo como"

    print(f"\n{Fore.CYAN}📝 {msg_generating}\n")

    content = ""
    for section in sections:
        print(f"{Fore.GREEN}✓ {msg_adding}: {section}")
        content += get_section_content(section, lang) + "\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n{Fore.GREEN}✨ {msg_success}")
    print(f"{Fore.YELLOW}📂 {msg_saved}: {os.path.abspath('README.md')}")

def main() -> None:
    """Função principal do programa."""
    try:
        clear_screen()
        print_header()

        lang = select_language()
        sections = select_sections(lang)
        create_readme(sections, lang)

        print(f"\n{Fore.CYAN}{'='*80}")
        msg = "Process completed successfully!" if lang == "en" else "Processo finalizado com sucesso!"
        print(f"{Fore.GREEN}🎉 {msg}")
        print(f"{Fore.CYAN}{'='*80}")

    except KeyboardInterrupt:
        msg = "Program interrupted by user. Goodbye!" if lang == "en" else "Programa interrompido pelo usuário. Até logo!"
        print(f"\n\n{Fore.YELLOW}👋 {msg}")
        sys.exit(0)
    except Exception as e:
        msg = "Unexpected error" if lang == "en" else "Erro inesperado"
        print(f"\n{Fore.RED}❌ {msg}: {str(e)}")
        sys.exit(1)
