<p align="center">
  <picture><source media="(prefers-color-scheme: light)" srcset="assets/banner-en-light.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/banner-en-dark.svg"><img src="assets/banner-en-dark.svg" alt="Juan Frois, Solutions Developer, RPA Automation and Data" width="100%"></picture>
</p>

<p align="center"><em>From Operations to Engineering: solving complex problems with technology.</em></p>

<p align="center">🇧🇷 <a href="README.md">Português</a> &nbsp;·&nbsp; 🇺🇸 <b>English</b></p>

<div align="center">

<a href="https://www.linkedin.com/in/jfrois/"><picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/LinkedIn-f0f3f8?style=for-the-badge&logo=linkedin&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/LinkedIn-000000?style=for-the-badge&logo=linkedin&logoColor=7392E0"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-000000?style=for-the-badge&logo=linkedin&logoColor=7392E0"></picture></a> <a href="mailto:contatojuanfrois@gmail.com"><picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Email-f0f3f8?style=for-the-badge&logo=gmail&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Email-000000?style=for-the-badge&logo=gmail&logoColor=7392E0"><img alt="Email" src="https://img.shields.io/badge/Email-000000?style=for-the-badge&logo=gmail&logoColor=7392E0"></picture></a>

</div>

<picture><source media="(prefers-color-scheme: light)" srcset="assets/divider-light.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg"><img src="assets/divider-dark.svg" alt="" width="100%"></picture>

### 👨‍💻 About me

I've worked at companies like **Loft, QuintoAndar and VOSS Automotive**. That hybrid view of Operations and Technology taught me to spot real bottlenecks and build tools that solve them.

I use **Python** for Automation (RPA) and Data Analysis. My goal is to work in Software Engineering, delivering operational efficiency and strategic value, **not just code**.

### 📈 Impact in numbers

*Active user time: how long the person stays busy. The robot runs on its own afterwards.*

<p align="center">
  <picture><source media="(prefers-color-scheme: light)" srcset="assets/metric-processador-en-light.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/metric-processador-en-dark.svg"><img src="assets/metric-processador-en-dark.svg" alt="Order Processor: from 6 to 12 hours down to 20 seconds. Has run 8,000 orders in about 6 hours, unattended." width="400"></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="assets/metric-totvs-en-light.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/metric-totvs-en-dark.svg"><img src="assets/metric-totvs-en-dark.svg" alt="TOTVS Protheus Entry: from 30 minutes down to 20 seconds, 20 cases per cycle." width="400"></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="assets/metric-aftermarket-en-light.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/metric-aftermarket-en-dark.svg"><img src="assets/metric-aftermarket-en-dark.svg" alt="Aftermarket Analysis: from 3 hours per part to an instant answer, used by 4 people." width="400"></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="assets/metric-envio-en-light.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/metric-envio-en-dark.svg"><img src="assets/metric-envio-en-dark.svg" alt="New Cases Dispatch: from 100 to 500 sends a day, 3 to 5 times the manual volume." width="400"></picture>
</p>

<picture><source media="(prefers-color-scheme: light)" srcset="assets/divider-light.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg"><img src="assets/divider-dark.svg" alt="" width="100%"></picture>

### 🚀 Featured projects

<p align="center">
  <a href="https://github.com/JFrois/Analise-Aftermarket"><picture><source media="(prefers-color-scheme: light)" srcset="assets/card-aftermarket-en-light.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/card-aftermarket-en-dark.svg"><img src="assets/card-aftermarket-en-dark.svg" alt="Aftermarket Analysis: Python, Streamlit and SQL. Cross-references OEM customer data and instantly answers where parts are and which aftermarket opportunities exist." width="400"></picture></a>
  <a href="https://github.com/JFrois/RPA-Processamento_PDFs"><picture><source media="(prefers-color-scheme: light)" srcset="assets/card-processador-en-light.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/card-processador-en-dark.svg"><img src="assets/card-processador-en-dark.svg" alt="Order Processor (RPA): Python and Selenium. Downloads orders from the B2B portal, reads PDFs, consolidates into Excel and emails a notification." width="400"></picture></a>
  <a href="https://github.com/JFrois/Automa-o-de-Cadastro-de-Previs-o-de-Vendas---TOTVS-Protheus"><picture><source media="(prefers-color-scheme: light)" srcset="assets/card-totvs-en-light.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/card-totvs-en-dark.svg"><img src="assets/card-totvs-en-dark.svg" alt="TOTVS Protheus Entry: Python and RPA. Bot that enters sales forecasts into the ERP from a spreadsheet." width="400"></picture></a>
  <a href="https://github.com/JFrois/Envio-novos-casos---Python"><picture><source media="(prefers-color-scheme: light)" srcset="assets/card-envio-en-light.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/card-envio-en-dark.svg"><img src="assets/card-envio-en-dark.svg" alt="New Cases Dispatch: Python and Zapier. Consolidates data and sends 300 to 500 cases a day with one click." width="400"></picture></a>
</p>

<details>
<summary><b>⚙️ View the Order Processor architecture</b></summary>

```mermaid
graph LR
    A[🌐 B2B Portal] -->|Scraping & Download| B(🤖 Python Robot)
    B -->|Data Extraction| C{📄 PDF Reading}
    C -->|Structuring| D[(📊 Excel Report)]
    D -->|Automatic Dispatch| E[✉️ Email Notification]

    style A fill:#0d1117,stroke:#73C2A9,stroke-width:2px,color:#73C2A9
    style B fill:#000000,stroke:#7392E0,stroke-width:2px,color:#7392E0
    style C fill:#0d1117,stroke:#71A5CA,stroke-width:2px,color:#71A5CA
    style D fill:#000000,stroke:#7392E0,stroke-width:2px,color:#7392E0
    style E fill:#0d1117,stroke:#73C2A9,stroke-width:2px,color:#73C2A9
```

</details>

<picture><source media="(prefers-color-scheme: light)" srcset="assets/divider-light.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg"><img src="assets/divider-dark.svg" alt="" width="100%"></picture>

### 💻 Stack

**Core:**
<picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Python-f0f3f8?style=for-the-badge&logo=python&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=7392E0"><img src="https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=7392E0" alt="Python"></picture> <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/SQL_Server-f0f3f8?style=for-the-badge&logo=microsoftsqlserver&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/SQL_Server-000000?style=for-the-badge&logo=microsoftsqlserver&logoColor=7392E0"><img src="https://img.shields.io/badge/SQL_Server-000000?style=for-the-badge&logo=microsoftsqlserver&logoColor=7392E0" alt="SQL Server"></picture> <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/PostgreSQL-f0f3f8?style=for-the-badge&logo=postgresql&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/PostgreSQL-000000?style=for-the-badge&logo=postgresql&logoColor=7392E0"><img src="https://img.shields.io/badge/PostgreSQL-000000?style=for-the-badge&logo=postgresql&logoColor=7392E0" alt="PostgreSQL"></picture> <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Streamlit-f0f3f8?style=for-the-badge&logo=streamlit&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Streamlit-000000?style=for-the-badge&logo=streamlit&logoColor=7392E0"><img src="https://img.shields.io/badge/Streamlit-000000?style=for-the-badge&logo=streamlit&logoColor=7392E0" alt="Streamlit"></picture> <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Selenium-f0f3f8?style=for-the-badge&logo=selenium&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Selenium-000000?style=for-the-badge&logo=selenium&logoColor=7392E0"><img src="https://img.shields.io/badge/Selenium-000000?style=for-the-badge&logo=selenium&logoColor=7392E0" alt="Selenium"></picture> <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Power_BI-f0f3f8?style=for-the-badge&logo=powerbi&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Power_BI-000000?style=for-the-badge&logo=powerbi&logoColor=7392E0"><img src="https://img.shields.io/badge/Power_BI-000000?style=for-the-badge&logo=powerbi&logoColor=7392E0" alt="Power BI"></picture>

**Also use:**
<picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/JavaScript-f0f3f8?style=for-the-badge&logo=javascript&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/JavaScript-000000?style=for-the-badge&logo=javascript&logoColor=7392E0"><img src="https://img.shields.io/badge/JavaScript-000000?style=for-the-badge&logo=javascript&logoColor=7392E0" alt="JavaScript"></picture> <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Java-f0f3f8?style=for-the-badge&logo=openjdk&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Java-000000?style=for-the-badge&logo=openjdk&logoColor=7392E0"><img src="https://img.shields.io/badge/Java-000000?style=for-the-badge&logo=openjdk&logoColor=7392E0" alt="Java"></picture> <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/C-f0f3f8?style=for-the-badge&logo=c&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/C-000000?style=for-the-badge&logo=c&logoColor=7392E0"><img src="https://img.shields.io/badge/C-000000?style=for-the-badge&logo=c&logoColor=7392E0" alt="C"></picture> <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/HTML5_%26_CSS3-f0f3f8?style=for-the-badge&logo=html5&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/HTML5_%26_CSS3-000000?style=for-the-badge&logo=html5&logoColor=7392E0"><img src="https://img.shields.io/badge/HTML5_%26_CSS3-000000?style=for-the-badge&logo=html5&logoColor=7392E0" alt="HTML/CSS"></picture> <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/MySQL-f0f3f8?style=for-the-badge&logo=mysql&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/MySQL-000000?style=for-the-badge&logo=mysql&logoColor=7392E0"><img src="https://img.shields.io/badge/MySQL-000000?style=for-the-badge&logo=mysql&logoColor=7392E0" alt="MySQL"></picture> <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Docker-f0f3f8?style=for-the-badge&logo=docker&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Docker-000000?style=for-the-badge&logo=docker&logoColor=7392E0"><img src="https://img.shields.io/badge/Docker-000000?style=for-the-badge&logo=docker&logoColor=7392E0" alt="Docker"></picture> <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Git_%26_GitHub-f0f3f8?style=for-the-badge&logo=github&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Git_%26_GitHub-000000?style=for-the-badge&logo=github&logoColor=7392E0"><img src="https://img.shields.io/badge/Git_%26_GitHub-000000?style=for-the-badge&logo=github&logoColor=7392E0" alt="Git"></picture> <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Jira_%26_Confluence-f0f3f8?style=for-the-badge&logo=jira&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Jira_%26_Confluence-000000?style=for-the-badge&logo=jira&logoColor=7392E0"><img src="https://img.shields.io/badge/Jira_%26_Confluence-000000?style=for-the-badge&logo=jira&logoColor=7392E0" alt="Jira"></picture> <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Postman-f0f3f8?style=for-the-badge&logo=postman&logoColor=3f5fb8"><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Postman-000000?style=for-the-badge&logo=postman&logoColor=7392E0"><img src="https://img.shields.io/badge/Postman-000000?style=for-the-badge&logo=postman&logoColor=7392E0" alt="Postman"></picture>

<picture><source media="(prefers-color-scheme: light)" srcset="assets/divider-light.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg"><img src="assets/divider-dark.svg" alt="" width="100%"></picture>

### 📊 GitHub activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/JFrois/JFrois/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/JFrois/JFrois/output/github-snake.svg">
  <img alt="Snake animation over the contribution graph" src="https://raw.githubusercontent.com/JFrois/JFrois/output/github-snake.svg" width="100%">
</picture>

<p align="center">
  <picture><source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=JFrois&layout=compact&hide_border=true&bg_color=ffffff&title_color=3f5fb8&text_color=57606a"><source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=JFrois&layout=compact&hide_border=true&bg_color=000000&title_color=7392E0&text_color=71A5CA"><img src="https://github-readme-stats.vercel.app/api/top-langs/?username=JFrois&layout=compact&hide_border=true&bg_color=000000&title_color=7392E0&text_color=71A5CA" alt="Most used languages" /></picture>
</p>

<picture><source media="(prefers-color-scheme: light)" srcset="assets/divider-light.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg"><img src="assets/divider-dark.svg" alt="" width="100%"></picture>

<p align="center">
  <picture><source media="(prefers-color-scheme: light)" srcset="assets/footer-en-light.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/footer-en-dark.svg"><img src="assets/footer-en-dark.svg" alt="Let's automate something together? Reach me on LinkedIn or email." width="100%"></picture>
</p>
