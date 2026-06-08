# Análise da Cesta Básica no Brasil

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/Dashboard-GitHub%20Pages-222222?style=flat&logo=github&logoColor=white)

Análise exploratória da evolução do preço da cesta básica e das horas de trabalho necessárias para sua aquisição em capitais do Sudeste brasileiro, com dados da pesquisa nacional do DIEESE.

🔗 **[Ver dashboard publicado](https://enzo-going.github.io/analise-cesta-basica-brasil/)**

---

## Cidades analisadas

São Paulo · Rio de Janeiro · Belo Horizonte · Vitória

---

## O que o projeto investiga

- Evolução histórica do preço da cesta básica por cidade
- Horas de trabalho necessárias para aquisição (salário mínimo como referência)
- Comparativo entre capitais ao longo do tempo
- Tendências e sazonalidade nos dados DIEESE

---

## Estrutura

```
├── data/
│   ├── raw/            # Arquivos brutos do DIEESE
│   └── processed/      # Dados tratados
├── notebooks/          # Análise exploratória
├── src/                # Scripts de processamento e geração de gráficos
└── output/
    ├── charts/         # Gráficos exportados
    └── tables/         # Tabelas geradas
```

---

## Como executar

```bash
git clone https://github.com/enzo-going/analise-cesta-basica-brasil.git
cd analise-cesta-basica-brasil
pip install -r requirements.txt
jupyter notebook notebooks/
```

---

## Origem

Projeto originado de pesquisa acadêmica, reestruturado como portfólio técnico reproduzível com pipeline de dados documentado e interface web publicada.
