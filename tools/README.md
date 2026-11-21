# tools

## make_assets.py

Gera os SVGs usados nos perfis (`README.md` em português e `README.en.md` em inglês).
São 2 idiomas × 2 temas (claro e escuro), mais o divisor, num total de 42 arquivos em `assets/`.

```bash
python3 tools/make_assets.py
```

Não precisa instalar nada. Para mudar textos ou métricas, edite o dicionário `LANGS`
(português e inglês) no topo do bloco final do script; para mudar cores, edite `THEMES`.
Depois de gerar, confira se os alts e os textos dos dois README continuam batendo com as imagens.
