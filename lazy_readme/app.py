import os
from dotenv import load_dotenv
import google.generativeai as genai


def setup_gemini():
    if os.path.exists(".env"):
        load_dotenv()
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            print("\033[31mAPI Key not found in .env. Please provide it.\033[0m")
            return setup_gemini()
    else:
        api_key = input("Enter your Gemini API Key: ").strip()
        with open(".env", "w") as file:
            file.write(f"GEMINI_API_KEY={api_key}")

    try:
        genai.configure(api_key=api_key)
        gemini_model = genai.GenerativeModel("gemini-1.5-flash")
        return gemini_model
    except Exception as e:
        print(f"\033[31mInvalid API Key: {e}\033[0m")
        return setup_gemini()


def project_details():
    """Collects project name and description."""
    while True:
        try:
            project_name = input("\033[32mEnter the project name: \033[0m").strip()
            if not project_name:
                print("\033[31mProject name cannot be empty.\033[0m")
                continue

            project_description = input(
                "\033[32mDescribe your project: \033[0m"
            ).strip()
            if not project_description:
                print("\033[31mProject description cannot be empty.\033[0m")
                continue

            return {
                "project_name": project_name,
                "project_description": project_description,
            }
        except Exception as e:
            print(f"\033[31mAn error occurred: {e}\033[0m")


def ask_preference(section_name):
    """Asks user if they want a specific section."""
    while True:
        try:
            response = (
                input(f"\033[32mDo you want a {section_name} section? (y/n): \033[0m")
                .strip()
                .lower()
            )
            if response not in ["y", "n"]:
                print("\033[31mInvalid input. Please enter 'y' or 'n'.\033[0m")
                continue
            return response == "y"
        except Exception as e:
            print(f"\033[31mAn error occurred: {e}\033[0m")


def user_preferences():
    """Collects user preferences for README sections."""
    sections = [
        "requisites and installation",
        "usage",
        "documentation",
        "contribution",
        "credits",
        "license",
        "contact",
    ]
    return {section: ask_preference(section) for section in sections}


def generate_header(project_data):
    """Generates the README header with project details."""
    genai_model = setup_gemini()
    gemini_response = genai_model.generate_content(
        f"I want you generate a describe in a few lines the project {project_data['project_name']}, the project is about {project_data['project_description']}"
    )
    with open("RESULT.md", "w", encoding="utf-8") as file:
        file.write(
            f"<div align='center'>\n\n # 🔨 {project_data['project_name']}\n\n ### About this project \n\n <p style='width:500px'>{gemini_response.text}</p>\n</div>\n\n<br/>\n<br/>\n<br/>\n"
        )


def generate_readme():
    """Generates the README file based on user preferences."""
    project_data = project_details()
    generate_header(project_data)

    preferences = user_preferences()

    with open("README.md", "a", encoding="utf-8") as file:
        if preferences["requisites and installation"]:
            requisites_installation = [
                "# **📊 Prerequisites and Installation**\n\n",
                "### Prerequisites\n\n",
                "List any tools, libraries, or environments required to run the project.\n\n",
                "### 1. Clone the repository\n\n",
                "```bash\n",
                "  git clone https://github.com/username/project-name.git\n",
                "```\n\n",
                "### 2. Navigate to the project directory:\n\n",
                "```bash\n",
                "  git clone https://github.com/username/project-name.git\n",
                "```\n\n",
                "### 3. Install dependencies:\n\n",
                "```bash\n",
                "  npm install\n",
                "```\n\n",
                "<br/>\n\n",
                "🎉**Congratulations**, You're all set to start developing your project.\n\n",
                "<br/>\n",
                "<br/>\n",
                "<br/>\n",
            ]
            file.writelines(requisites_installation)
        if preferences["usage"]:
            file.write("## Usage\n\n")
            file.write("Explain how to use the project.\n\n")
        if preferences["documentation"]:
            file.write("## Documentation\n\n")
            file.write("Include links or instructions for documentation.\n\n")
        if preferences["contribution"]:
            file.write("## Contribution\n\n")
            file.write("Provide guidelines on how to contribute to the project.\n\n")
        if preferences["credits"]:
            file.write("## Credits\n\n")
            file.write("Acknowledge contributors or resources used in the project.\n\n")
        if preferences["license"]:
            file.write("## License\n\n")
            file.write("Specify the license for the project.\n\n")
        if preferences["contact"]:
            file.write("## Contact\n\n")
            file.write("Provide contact details for inquiries.\n\n")

    print("\033[32mREADME.md generated successfully!\033[0m")


generate_readme()
