import requests
from pathlib import Path

# URL do seu dashboard público da Alura
API_URL = "https://www.alura.com.br/api/dashboard/8b6930eefca6d579d24a4a3c73c4cd76a450a20f6842a0de1b6417edcb02dee8"

def generate_courses_markdown(data):
    """Gera a tabela Markdown para os cursos em andamento."""
    lines = ["#### Cursos em Andamento", "| Curso | Progresso |", "| :--- | :---: |"]
    courses = data.get('courseProgresses', [])
    if not courses:
        lines.append("| Nenhum curso em andamento. | |")
    else:
        for course in courses:
            name = course.get('name', 'N/A')
            progress = course.get('progress', 0)
            lines.append(f"| {name} | `[ {progress}% ]` |")
    return "\n".join(lines)

def generate_degrees_markdown(data):
    """Gera a tabela Markdown para as formações e planos de estudo."""
    lines = ["#### Formações e Planos de Estudo", "| Trilha de Estudo | Tipo | Cursos Concluídos |", "| :--- | :--- | :---: |"]
    guides = data.get('guides', [])
    if not guides:
        lines.append("| Nenhuma formação encontrada. | | |")
    else:
        for guide in guides:
            name = guide.get('name', 'N/A')
            kind = guide.get('kind', 'DEGREE').replace('_', ' ').replace('USER GUIDE', 'Plano Pessoal').replace('CAREER PATH', 'Carreira').title()
            finished = guide.get('finishedCourses', 0)
            total = guide.get('totalCourses', 0)
            lines.append(f"| {name} | {kind} | `{finished} de {total}` |")
    return "\n".join(lines)

if __name__ == "__main__":
    try:
        print("Iniciando a atualização do README.")
        readme_path = Path("README.md")
        if not readme_path.is_file():
            raise FileNotFoundError("Arquivo README.md não encontrado.")

        # Busca os dados da Alura
        print("Buscando dados na API da Alura...")
        response = requests.get(API_URL)
        if response.status_code != 200:
            raise Exception(f"Falha ao buscar dados. Status: {response.status_code}")
        alura_data = response.json()
        print("Dados recebidos com sucesso.")

        # Gera os novos blocos de conteúdo
        courses_md = generate_courses_markdown(alura_data)
        degrees_md = generate_degrees_markdown(alura_data)

        # Lê o README original e reconstrói linha por linha
        new_readme_lines = []
        skip_section = None
        
        with open(readme_path, "r", encoding="utf-8") as f:
            for line in f:
                # Verifica se a linha é um marcador de início
                if "" in line:
                    skip_section = "ALURA_COURSES"
                    new_readme_lines.append(line)
                    new_readme_lines.append(courses_md + "\n")
                elif "" in line:
                    skip_section = "ALURA_DEGREES"
                    new_readme_lines.append(line)
                    new_readme_lines.append(degrees_md + "\n")
                # Verifica se a linha é um marcador de fim
                elif "" in line or "" in line:
                    skip_section = None
                    new_readme_lines.append(line)
                # Se não estivermos pulando uma seção, adiciona a linha original
                elif not skip_section:
                    new_readme_lines.append(line)
        
        # Salva o conteúdo reconstruído no arquivo
        print("Salvando o novo conteúdo no README.md...")
        readme_path.write_text("".join(new_readme_lines), encoding="utf-8")
        
        print("README.md atualizado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro fatal: {e}")
        exit(1)
