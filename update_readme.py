import requests
from pathlib import Path

API_URL = "https://www.alura.com.br/api/dashboard/8b6930eefca6d579d24a4a3c73c4cd76a450a20f6842a0de1b6417edcb02dee8"
README_PATH = Path("README.md")


def fetch_data(url):
    """Busca dados de uma URL e retorna o JSON."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Erro ao buscar dados da API: Status {response.status_code}")
    return response.json()


def generate_markdown_table(data, section):
    """Gera uma tabela Markdown para uma seção específica dos dados."""
    if section == "courses":
        header = [
            "#### Cursos em Andamento",
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

    if section == "degrees":
        header = [
            "#### Formações e Planos de Estudo",
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
    return ""


def replace_section_with_split(content, marker_name, new_block):
    """Substitui o conteúdo entre marcadores usando string.split()."""
    # Marcadores agora são criados com base no nome da seção
    start_marker = f""
    end_marker = f""
    
    try:
        # Divide o conteúdo do README em três partes: antes, dentro e depois dos marcadores
        before, rest = content.split(start_marker, 1)
        _, after = rest.split(end_marker, 1)
        
        # Reconstrói o conteúdo com o novo bloco de informações
        return f"{before}{start_marker}\n\n{new_block}\n\n{end_marker}{after}"
    except ValueError:
        print(f"Aviso: Marcador '{marker_name}' não encontrado no README.md.")
        return content


if __name__ == "__main__":
    try:
        readme_content = README_PATH.read_text(encoding="utf-8")
        alura_data = fetch_data(API_URL)
        
        # Gera a tabela de cursos
        courses_table = generate_markdown_table(alura_data, "courses")
        
        # Gera a tabela de formações
        degrees_table = generate_markdown_table(alura_data, "degrees")
        
        # Substitui a seção de cursos no README
        readme_content = replace_section_with_split(
            readme_content, "ALURA_COURSES", courses_table
        )
        
        # Substitui a seção de formações no README
        readme_content = replace_section_with_split(
            readme_content, "ALURA_DEGREES", degrees_table
        )
        
        README_PATH.write_text(readme_content, encoding="utf-8")
        print("✅ README atualizado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        exit(1)