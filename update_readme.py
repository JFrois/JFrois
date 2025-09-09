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
        raise Exception("Falha ao buscar dados da API da Alura.")
    return response.json()

def generate_courses_markdown(data):
    """Gera a tabela Markdown para os cursos em andamento."""
    markdown = "#### Cursos em Andamento\n"
    markdown += "| Curso | Progresso |\n"
    markdown += "| :--- | :---: |\n"
    for course in data.get('courseProgresses', []):
        name = course.get('name', 'N/A')
        progress = course.get('progress', 0)
        markdown += f"| {name} | `[ {progress}% ]` |\n"
    return markdown

def generate_degrees_markdown(data):
    """Gera a tabela Markdown para as formações e planos de estudo."""
    markdown = "#### Formações e Planos de Estudo\n"
    markdown += "| Trilha de Estudo | Tipo | Cursos Concluídos |\n"
    markdown += "| :--- | :--- | :---: |\n"
    for guide in data.get('guides', []):
        name = guide.get('name', 'N/A')
        kind = guide.get('kind', 'DEGREE').replace('_', ' ').replace('USER GUIDE', 'Plano Pessoal').replace('CAREER PATH', 'Carreira').title()
        finished = guide.get('finishedCourses', 0)
        total = guide.get('totalCourses', 0)
        markdown += f"| {name} | {kind} | `{finished} de {total}` |\n"
    return markdown

def update_readme(new_content, marker_name):
    """Atualiza uma seção específica do README.md."""
    readme_path = Path("README.md")
    if not readme_path.is_file():
        raise FileNotFoundError("README.md não encontrado.")

    start_marker = f""
    end_marker = f""
    
    content = readme_path.read_text(encoding='utf-8')
    
    # Usa expressão regular para substituir o conteúdo entre os marcadores
    pattern = re.compile(f"{re.escape(start_marker)}(.*?){re.escape(end_marker)}", re.DOTALL)
    new_readme_content = pattern.sub(f"{start_marker}\n{new_content}\n{end_marker}", content)
    
    readme_path.write_text(new_readme_content, encoding='utf-8')
    print(f"Seção '{marker_name}' do README atualizada com sucesso!")

if __name__ == "__main__":
    try:
        alura_data = fetch_alura_data()
        
        courses_md = generate_courses_markdown(alura_data)
        update_readme(courses_md, "ALURA_COURSES")
        
        degrees_md = generate_degrees_markdown(alura_data)
        update_readme(degrees_md, "ALURA_DEGREES")
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
