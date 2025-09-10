import requests
import re
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
        header = ["#### Cursos em Andamento", "| Curso | Progresso |", "| :--- | :---: |"]
        items = data.get('courseProgresses', [])
        if not items: return "\n".join(header + ["| Nenhum curso em andamento. | |"])
        
        rows = [f"| {item.get('name', 'N/A')} | `[ {item.get('progress', 0)}% ]` |" for item in items]
        return "\n".join(header + rows)

    if section == "degrees":
        header = ["#### Formações e Planos de Estudo", "| Trilha de Estudo | Tipo | Cursos Concluídos |", "| :--- | :--- | :---: |"]
        items = data.get('guides', [])
        if not items: return "\n".join(header + ["| Nenhuma formação encontrada. | | |"])
        
        rows = []
        for item in items:
            kind = item.get('kind', 'DEGREE').replace('_', ' ').replace('USER GUIDE', 'Plano Pessoal').replace('CAREER PATH', 'Carreira').title()
            rows.append(f"| {item.get('name', 'N/A')} | {kind} | `{item.get('finishedCourses', 0)} de {item.get('totalCourses', 0)}` |")
        return "\n".join(header + rows)
    
    return ""

def replace_section_in_text(text, marker_name, new_content):
    """Substitui o conteúdo entre marcadores em um texto."""
    # LINHAS CORRIGIDAS:
    start_marker = f""
    end_marker = f""
    
    pattern = re.compile(f"{re.escape(start_marker)}(.*?){re.escape(end_marker)}", re.DOTALL)
    
    # Adiciona quebras de linha para garantir o espaçamento correto no Markdown
    replacement = f"{start_marker}\n\n{new_content}\n\n{end_marker}"
    
    return pattern.sub(replacement, text)

if __name__ == "__main__":
    try:
        # 1. Garante que os marcadores existem no README
        readme_content = README_PATH.read_text(encoding="utf-8")
        if "" not in readme_content or "" not in readme_content:
            raise ValueError("Marcadores de seção da Alura não encontrados no README.md. Adicione etc.")

        # 2. Busca os dados da Alura
        alura_data = fetch_data(API_URL)
        
        # 3. Gera as novas seções de Markdown
        courses_table = generate_markdown_table(alura_data, "courses")
        degrees_table = generate_markdown_table(alura_data, "degrees")
        
        # 4. Substitui as seções no conteúdo do README
        readme_content = replace_section_in_text(readme_content, "ALURA_COURSES", courses_table)
        readme_content = replace_section_in_text(readme_content, "ALURA_DEGREES", degrees_table)
        
        # 5. Salva o novo conteúdo no arquivo README.md
        README_PATH.write_text(readme_content, encoding="utf-8")
        
        print("✅ README atualizado com sucesso!")

    except Exception as e:
        print(f"❌ Erro: {e}")
        exit(1)
