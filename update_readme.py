import requests
import re
from pathlib import Path

API_URL = "https://www.alura.com.br/api/dashboard/8b6930eefca6d579d24a4a3c73c4cd76a450a20f6842a0de1b6417edcb02dee8"
README_PATH = Path("README.md")

def fetch_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Erro ao buscar dados da API: Status {response.status_code}")
    return response.json()

def generate_markdown_table(data, section):
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
    start_marker = f""
    end_marker = f""
    pattern = re.compile(f"{re.escape(start_marker)}(.*?){re.escape(end_marker)}", re.DOTALL)
    replacement = f"{start_marker}\n{new_content}\n{end_marker}"
    return pattern.sub(replacement, text)

if __name__ == "__main__":
    try:
        print("--- PASSO 1: LENDO O ARQUIVO README.md ---")
        readme_content = README_PATH.read_text(encoding="utf-8")
        print(f"Leitura concluída. O arquivo tem {len(readme_content)} caracteres.")
        print("--- CONTEÚDO ORIGINAL LIDO ---")
        print(readme_content)
        print("---------------------------------")

        if "" not in readme_content:
            raise ValueError("Marcador ALURA_COURSES_START não encontrado!")
        
        print("\n--- PASSO 2: BUSCANDO DADOS DA ALURA ---")
        alura_data = fetch_data(API_URL)
        print("Dados da Alura obtidos com sucesso.")
        
        print("\n--- PASSO 3: GERANDO TABELAS MARKDOWN ---")
        courses_table = generate_markdown_table(alura_data, "courses")
        degrees_table = generate_markdown_table(alura_data, "degrees")
        print("--- TABELA DE CURSOS ---")
        print(courses_table)
        print("--------------------------")
        print("--- TABELA DE FORMAÇÕES ---")
        print(degrees_table)
        print("---------------------------")

        print("\n--- PASSO 4: SUBSTITUINDO SEÇÕES ---")
        readme_content = replace_section_in_text(readme_content, "ALURA_COURSES", courses_table)
        readme_content = replace_section_in_text(readme_content, "ALURA_DEGREES", degrees_table)
        print("Substituição em memória concluída.")

        print("\n--- PASSO 5: PREPARANDO PARA SALVAR ---")
        print(f"O conteúdo final a ser salvo tem {len(readme_content)} caracteres.")
        print("--- CONTEÚDO FINAL A SER SALVO ---")
        print(readme_content)
        print("------------------------------------")
        
        README_PATH.write_text(readme_content, encoding="utf-8")
        
        print("\n✅ Script Python finalizado com sucesso.")

    except Exception as e:
        print(f"❌ Erro no script Python: {e}")
        exit(1)