"""Gera os SVGs do perfil (banner, cartoes, cards, divisor, rodape).

Saida: 2 idiomas (pt, en) x 2 temas (dark, light) em assets/.
Uso:  python3 tools/make_assets.py [pasta_de_saida]
Sem dependencias externas (so biblioteca padrao do Python 3).
"""
import os, sys
from xml.sax.saxutils import escape as esc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "assets")
os.makedirs(OUT, exist_ok=True)

MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
SANS = "-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
THEMES = {
 "dark":  dict(BG="#0d1117", BORDER="#1f2a44", BLUE="#7392E0", GREEN="#73C2A9", SKY="#71A5CA", CYAN="#4DD0E1", TXT="#e6edf3", MUTED="#8b9bb4", GLOW1=".30", GLOW2=".22", DOT=".18"),
 "light": dict(BG="#ffffff", BORDER="#d0d7de", BLUE="#3f5fb8", GREEN="#1d8a6a", SKY="#2f6a9e", CYAN="#0b7285", TXT="#1f2328", MUTED="#57606a", GLOW1=".13", GLOW2=".12", DOT=".16"),
}
def set_theme(name):
    globals().update(THEMES[name])
set_theme("dark")

def svg(w, h, body, title, desc=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">
<title id="t">{esc(title)}</title><desc id="d">{esc(desc or title)}</desc>
<defs>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="{GREEN}"/></linearGradient>
<linearGradient id="gv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="{GREEN}"/></linearGradient>
<pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1" fill="{BLUE}" opacity="{DOT}"/></pattern>
<radialGradient id="glow"><stop offset="0" stop-color="{BLUE}" stop-opacity="{GLOW1}"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
<radialGradient id="glow2"><stop offset="0" stop-color="{GREEN}" stop-opacity="{GLOW2}"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></radialGradient>
</defs>
<style>
text{{font-family:{MONO}}}
.sans{{font-family:{SANS}}}
@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
@keyframes pulse{{0%{{r:5;opacity:.9}}100%{{r:14;opacity:0}}}}
@keyframes flow{{to{{stroke-dashoffset:-24}}}}
.cur{{animation:blink 1.1s steps(1) infinite}}
.pulse{{animation:pulse 2s ease-out infinite}}
.flow{{animation:flow 1.2s linear infinite}}
@media (prefers-reduced-motion:reduce){{.cur,.pulse,.flow{{animation:none}}}}
</style>
{body}
</svg>
'''

def panel(w, h, r=16):
    return (f'<rect x=".75" y=".75" width="{w-1.5}" height="{h-1.5}" rx="{r}" fill="{BG}" stroke="{BORDER}" stroke-width="1.5"/>'
            f'<rect x=".75" y=".75" width="{w-1.5}" height="{h-1.5}" rx="{r}" fill="url(#dots)"/>')

def chips(x, y, items):
    out, cx = [], x
    for it in items:
        wd = int(len(it) * 7.8 + 22)
        out.append(f'<rect x="{cx}" y="{y}" width="{wd}" height="26" rx="13" fill="{BLUE}" fill-opacity=".12" stroke="{BLUE}" stroke-opacity=".55"/>'
                   f'<text x="{cx + wd/2}" y="{y+17.5}" font-size="12.5" fill="{SKY}" text-anchor="middle">{esc(it)}</text>')
        cx += wd + 10
    return "".join(out)

# ---------- banner ----------
def banner(L):
    w, h = 1200, 300
    nodes = list(zip((840, 940, 1040, 1140), L["nodes"]))
    pipe = f'<line x1="840" y1="170" x2="1140" y2="170" stroke="{BORDER}" stroke-width="2"/>'
    pipe += f'<rect x="840" y="168.75" width="300" height="2.5" fill="url(#g)" opacity=".55"/><line class="flow" x1="840" y1="170" x2="1140" y2="170" stroke="{CYAN}" stroke-width="2" stroke-dasharray="3 21" stroke-linecap="round"/>'
    for i, (x, lab) in enumerate(nodes):
        col = GREEN if i % 2 == 0 else BLUE
        pipe += (f'<circle cx="{x}" cy="170" r="22" fill="{BG}" stroke="{col}" stroke-width="2"/>'
                 f'<circle cx="{x}" cy="170" r="7" fill="{col}"/>'
                 f'<text x="{x}" y="217" font-size="13" fill="{MUTED}" text-anchor="middle">{lab}</text>')
    body = panel(w, h, 18)
    body += f'<circle cx="980" cy="150" r="260" fill="url(#glow)"/><circle cx="180" cy="300" r="240" fill="url(#glow2)"/>'
    body += f'<text x="60" y="70" font-size="16" fill="{CYAN}">{L["kicker"]}</text>'
    body += f'<text x="58" y="148" font-size="68" font-weight="700" fill="url(#g)">Juan Frois</text>'
    body += f'<text x="60" y="196" font-size="23" fill="{TXT}" class="sans">{L["headline"]}</text>'
    body += f'<text x="60" y="246" font-size="20" fill="{GREEN}">&gt; {L["prompt"]}<tspan class="cur" fill="{CYAN}">█</tspan></text>'
    body += pipe
    body += (f'<circle class="pulse" cx="1062" cy="52" r="5" fill="{GREEN}"/><circle cx="1062" cy="52" r="5" fill="{GREEN}"/>'
             f'<text x="1078" y="57" font-size="14" fill="{GREEN}">online</text>')
    return svg(w, h, body, L["banner_alt"])

# ---------- metric cards ----------
def metric(label, value, sub1, sub2, value_size=44):
    w, h = 560, 170
    body = panel(w, h, 14)
    body += f'<rect x="1.5" y="28" width="4" height="40" rx="2" fill="url(#gv)"/>'
    body += f'<text x="26" y="40" font-size="13" letter-spacing="1.5" fill="{CYAN}">{esc(label)}</text>'
    body += f'<text x="24" y="102" font-size="{value_size}" font-weight="700" fill="url(#g)">{esc(value)}</text>'
    body += f'<text x="26" y="132" font-size="13.5" fill="{MUTED}">{esc(sub1)}</text>'
    body += f'<text x="26" y="152" font-size="13.5" fill="{MUTED}">{esc(sub2)}</text>'
    return svg(w, h, body, f"{label}: {value}", f"{sub1} {sub2}")

# ---------- project cards ----------
def project(tag, title, lines, stack):
    w, h = 560, 230
    body = panel(w, h, 14)
    body += f'<circle cx="28" cy="30" r="5" fill="#ff5f56"/><circle cx="46" cy="30" r="5" fill="#ffbd2e"/><circle cx="64" cy="30" r="5" fill="#27c93f"/>'
    body += f'<text x="534" y="34" font-size="12" letter-spacing="1.2" fill="{CYAN}" text-anchor="end">{esc(tag)}</text>'
    body += f'<line x1="1" y1="50" x2="{w-1}" y2="50" stroke="{BORDER}"/>'
    body += f'<text x="26" y="86" font-size="22" font-weight="700" fill="{TXT}">{esc(title)}</text>'
    for i, ln in enumerate(lines):
        body += f'<text x="26" y="{116 + i*21}" font-size="13.5" fill="{MUTED}">{esc(ln)}</text>'
    body += chips(26, 184, stack)
    return svg(w, h, body, title, " ".join(lines))

# ---------- divider / footer ----------
def divider():
    w, h = 1200, 28
    body = (f'<line x1="0" y1="14" x2="{w}" y2="14" stroke="{BORDER}" stroke-width="2"/>'
            f'<rect x="300" y="13" width="600" height="2" fill="url(#g)"/>'
            f'<circle cx="300" cy="14" r="4" fill="{BLUE}"/><circle cx="600" cy="14" r="6" fill="{BG}" stroke="url(#g)" stroke-width="2"/>'
            f'<circle cx="600" cy="14" r="2.5" fill="{GREEN}"/><circle cx="900" cy="14" r="4" fill="{GREEN}"/>')
    return svg(w, h, body, "Divisor de seção")

def footer(L):
    w, h = 1200, 120
    body = panel(w, h, 16)
    body += f'<circle cx="600" cy="150" r="220" fill="url(#glow)"/>'
    body += f'<text x="600" y="58" font-size="22" font-weight="700" fill="url(#g)" text-anchor="middle">{L["footer1"]}</text>'
    body += f'<text x="600" y="88" font-size="14" fill="{MUTED}" text-anchor="middle">&gt; {L["footer2"]}<tspan class="cur" fill="{CYAN}">█</tspan></text>'
    return svg(w, h, body, L["footer_alt"])

LANGS = {
"pt": dict(
  nodes=["portal","robô","dados","e-mail"], kicker="// automação · dados · python", headline="Desenvolvedor de Soluções  |  Automação (RPA)  |  Dados",
  prompt="eliminando trabalho manual", banner_alt="Juan Frois, Desenvolvedor de Soluções, Automação (RPA) e Dados",
  footer1="// vamos automatizar algo juntos?", footer2="contato pelo LinkedIn ou e-mail",
  footer_alt="Vamos automatizar algo juntos? Contato pelo LinkedIn ou e-mail",
  metrics=[
   ("processador","PROCESSADOR DE PEDIDOS","6–12 h → 20 s","tempo ativo do usuário (ciclo de ~1.000 PDFs)","já rodou 8.000 pedidos em ~6 h sem supervisão",44),
   ("totvs","CADASTRO TOTVS PROTHEUS","30 min → 20 s","20 casos por ciclo, ~1min30 cada à mão","agora: login + upload da planilha",44),
   ("aftermarket","ANÁLISE AFTERMARKET","3 h → instantâneo","por peça (3 a 4 por dia), antes às vezes dias","usado por todo o time (4 pessoas)",40),
   ("envio","ENVIO DE NOVOS CASOS","100 → 500 /dia","3x a 5x o volume manual (~2 h para 100 casos)","agora: um clique e o envio roda sozinho",44)],
  cards=[
   ("aftermarket","BI · ESTRATÉGIA","Análise Aftermarket",["Cruza dados de clientes OEM e responde na hora onde","estão as peças e as oportunidades de reposição.","Aplicação corporativa para a VOSS Automotive."],["Python","Streamlit","SQL"]),
   ("processador","RPA · DESKTOP","Processador de Pedidos",["Baixa os pedidos do portal B2B, lê os PDFs, consolida","em Excel e notifica por e-mail. Já processou 8.000","pedidos em ~6 h, sem supervisão."],["Python","Selenium"]),
   ("totvs","RPA · ERP","Cadastro TOTVS Protheus",["Bot que cadastra a previsão de vendas no ERP a partir","de uma planilha: 20 casos em ~20 s de intervenção,","contra ~30 min feitos à mão."],["Python","RPA"]),
   ("envio","AUTOMAÇÃO · DADOS","Envio de Novos Casos",["Consolida os dados (ex.: ITBI) e envia de 300 a 500","casos por dia com um clique, contra ~100 enviados","manualmente."],["Python","Zapier"])]),
"en": dict(
  nodes=["portal","robot","data","email"], kicker="// automation · data · python", headline="Solutions Developer  |  RPA Automation  |  Data",
  prompt="eliminating manual work", banner_alt="Juan Frois, Solutions Developer, RPA Automation and Data",
  footer1="// let's automate something together?", footer2="reach me on LinkedIn or email",
  footer_alt="Let's automate something together? Reach me on LinkedIn or email",
  metrics=[
   ("processador","ORDER PROCESSOR","6–12 h → 20 s","active user time (~1,000-PDF cycle)","ran 8,000 orders in ~6 h, unattended",44),
   ("totvs","TOTVS PROTHEUS ENTRY","30 min → 20 s","20 cases per cycle, ~1m30 each by hand","now: login + spreadsheet upload",44),
   ("aftermarket","AFTERMARKET ANALYSIS","3 h → instant","per part (3–4 a day), sometimes days before","used by the whole team (4 people)",44),
   ("envio","NEW CASES DISPATCH","100 → 500 /day","3x to 5x the manual volume (~2 h for 100)","now: one click, runs on its own",44)],
  cards=[
   ("aftermarket","BI · STRATEGY","Aftermarket Analysis",["Cross-references OEM customer data and instantly","answers where parts are and which aftermarket","opportunities exist. Corporate app, VOSS Automotive."],["Python","Streamlit","SQL"]),
   ("processador","RPA · DESKTOP","Order Processor",["Downloads orders from the B2B portal, reads PDFs,","consolidates into Excel and emails a notification.","Has run 8,000 orders in ~6 h, unattended."],["Python","Selenium"]),
   ("totvs","RPA · ERP","TOTVS Protheus Entry",["Bot that enters sales forecasts into the ERP from a","spreadsheet: 20 cases in ~20 s of user time,","versus ~30 min by hand."],["Python","RPA"]),
   ("envio","AUTOMATION · DATA","New Cases Dispatch",["Consolidates data (e.g. ITBI) and sends 300 to 500","cases a day with one click, versus ~100 sent","manually."],["Python","Zapier"])]),
}

def build(lang):
    L = LANGS[lang]
    out = {f"banner-{lang}": banner(L), f"footer-{lang}": footer(L)}
    for key, label, val, s1, s2, vs in L["metrics"]:
        out[f"metric-{key}-{lang}"] = metric(label, val, s1, s2, value_size=vs)
    for key, tag, title, lines, stack in L["cards"]:
        out[f"card-{key}-{lang}"] = project(tag, title, lines, stack)
    return out

for theme in THEMES:
    set_theme(theme)
    files = {"divider": divider()}
    for lang in LANGS:
        files.update(build(lang))
    for name, content in files.items():
        with open(os.path.join(OUT, f"{name}-{theme}.svg"), "w", encoding="utf-8") as f:
            f.write(content)
print("ok", len(files) * len(THEMES), "arquivos")
