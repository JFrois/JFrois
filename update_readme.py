import requests
import re
from pathlib import Path

# URL do seu dashboard público da Alura
API_URL = "https://www.alura.com.br/api/dashboard/8b6930eefca6d579d24a4a3c73c4cd76a450a20f6842a0de1b6417edcb02dee8"


def fetch_alura_data():
    """Busca e processa os dados da API da Alura."""
    print("Buscando dados na API da Alura...")
    response = requests.get(API_URL)
    if response.status_code != 200:
        raise Exception(f"Falha ao buscar dados. Status: {response.status_code}")
    print("Dados recebidos com sucesso.")
    return response.json()


def generate_courses_markdown(data):
    """Gera a tabela Markdown para os cursos em andamento."""
    markdown = "#### Cursos em Andamento\n"
    markdown += "| Curso | Progresso |\n"
    markdown += "| :--- | :---: |\n"
    courses = data.get("courseProgresses", [])
    if not courses:
        return markdown + "| Nenhum curso em andamento. |\n"
    for course in courses:
        name = course.get("name", "N/A")
        progress = course.get("progress", 0)
        markdown += f"| {name} | `[ {progress}% ]` |\n"
    return markdown


def generate_degrees_markdown(data):
    """Gera a tabela Markdown para as formações e planos de estudo."""
    markdown = "#### Formações e Planos de Estudo\n"
    markdown += "| Trilha de Estudo | Tipo | Cursos Concluídos |\n"
    markdown += "| :--- | :--- | :---: |\n"
    guides = data.get("guides", [])
    if not guides:
        return markdown + "| Nenhuma formação encontrada. | | |\n"
    for guide in guides:
        name = guide.get("name", "N/A")
        kind = (
            guide.get("kind", "DEGREE")
            .replace("_", " ")
            .replace("USER GUIDE", "Plano Pessoal")
            .replace("CAREER PATH", "Carreira")
            .title()
        )
        finished = guide.get("finishedCourses", 0)
        total = guide.get("totalCourses", 0)
        markdown += f"| {name} | {kind} | `{finished} de {total}` |\n"
    return markdown


def update_readme_section(content, new_section_content, marker_name):
    """Atualiza uma seção do conteúdo do README com base nos marcadores."""
    start_marker = f""
    end_marker = f""

    pattern = re.compile(
        f"{re.escape(start_marker)}(.*?){re.escape(end_marker)}", re.DOTALL
    )

    # Substitui o conteúdo entre os marcadores pelo novo conteúdo
    new_content = pattern.sub(
        f"{start_marker}\n{new_section_content}\n{end_marker}", content
    )
    return new_content


if __name__ == "__main__":
    try:
        readme_path = Path("README.md")
        if not readme_path.is_file():
            raise FileNotFoundError("Arquivo README.md não encontrado.")

        # Lê o conteúdo original com a codificação correta
        current_readme_content = readme_path.read_text(encoding="utf-8")

        alura_data = fetch_alura_data()

        # Gera o novo conteúdo para cada seção
        courses_md = generate_courses_markdown(alura_data)
        degrees_md = generate_degrees_markdown(alura_data)

        # Atualiza o conteúdo na memória
        updated_content = update_readme_section(
            current_readme_content, courses_md, "ALURA_COURSES"
        )
        updated_content = update_readme_section(
            updated_content, degrees_md, "ALURA_DEGREES"
        )

        # Salva o arquivo final de uma vez, com a codificação correta
        readme_path.write_text(updated_content, encoding="utf-8")

        print("README.md atualizado com sucesso!")

    except Exception as e:
        # Imprime o erro e sai com um código de erro para falhar o workflow
        print(f"Ocorreu um erro: {e}")
        exit(1)
