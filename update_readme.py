import requests
from pathlib import Path
import re

API_URL = "https://www.alura.com.br/api/dashboard/8b6930eefca6d579d24a4a3c73c4cd76a450a20f6842a0de1b6417edcb02dee8"
README_PATH = Path("README.md")
START_MARKER = "<!-- ALURA:START -->"
END_MARKER = "<!-- ALURA:END -->"


def fetch_data(url):
    """Busca dados de uma URL e retorna o JSON."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Erro ao buscar dados da API: Status {response.status_code}")
    return response.json()


def generate_courses_table(data):
    """Gera a tabela Markdown para os cursos em andamento."""
    header = [
        "#### 📚 Cursos em Andamento",
        "| Curso | Progresso |",
        "| :--- | :---: |",
    ]
    items = data.get("courseProgresses", [])
    if not items:
        return "\n".join(header + ["| Nenhum curso em andamento no momento. | - |"])

    rows = [
        f"| {item.get('name', 'N/A')} | `[ {item.get('progress', 0)}% ]` |"
        for item in items
    ]
    return "\n".join(header + rows)


def generate_degrees_table(data):
    """Gera a tabela Markdown para as formações."""
    header = [
        "#### 🎓 Formações e Planos de Estudo",
        "| Trilha de Estudo | Tipo | Cursos Concluídos |",
        "| :--- | :--- | :---: |",
    ]
    items = data.get("guides", [])
    if not items:
        return "\n".join(
            header + ["| Nenhuma formação em andamento no momento. | - | - |"]
        )

    rows = []
    for item in items:
        kind = (
            item.get("kind", "DEGREE")
            .replace("_", " ")
            .replace("USER GUIDE", "Plano Pessoal")
            .replace("CAREER PATH", "Carreira")
            .title()
        )
        rows.append(
            f"| {item.get('name', 'N/A')} | {kind} | `{item.get('finishedCourses', 0)} de {item.get('totalCourses', 0)}` |"
        )
    return "\n".join(header + rows)


def update_readme_section(readme_content, new_content):
    """Atualiza ou insere a seção da Alura no README."""
    pattern = re.compile(
        f"{re.escape(START_MARKER)}(.*?){re.escape(END_MARKER)}", re.DOTALL
    )

    replacement_block = f"{START_MARKER}\n\n{new_content}\n\n{END_MARKER}"

    new_readme_content, num_replacements = pattern.subn(
        replacement_block, readme_content
    )

    # Se não encontrou os marcadores, insere após a seção da Alura
    if num_replacements == 0:
        marker_section = "### 👨‍🏫 Meus Estudos na Alura"
        if marker_section in readme_content:
            new_readme_content = readme_content.replace(
                marker_section,
                f"{marker_section}\n\n{replacement_block}",
            )
        else:
            # fallback: adiciona no final
            new_readme_content = readme_content.strip() + "\n\n" + replacement_block

    return new_readme_content


if __name__ == "__main__":
    try:
        readme_content = README_PATH.read_text(encoding="utf-8")
        alura_data = fetch_data(API_URL)

        # Gera as duas tabelas
        courses_table = generate_courses_table(alura_data)
        degrees_table = generate_degrees_table(alura_data)

        # Combina as tabelas em um único bloco
        full_markdown_block = f"{courses_table}\n\n{degrees_table}"

        # Atualiza o conteúdo do README
        new_readme = update_readme_section(readme_content, full_markdown_block)

        README_PATH.write_text(new_readme, encoding="utf-8")
        print("✅ README atualizado com sucesso!")

    except Exception as e:
        print(f"❌ Erro: {e}")
        exit(1)
