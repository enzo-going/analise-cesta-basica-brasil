# Análise da Cesta Básica no Brasil

Projeto de análise exploratória de dados sobre a evolução do preço da cesta básica e das horas de trabalho necessárias para sua aquisição em capitais da região Sudeste do Brasil.

## Acesso ao projeto

A interface web inicial do projeto está disponível em:

https://enzo-going.github.io/analise-cesta-basica-brasil/


O objetivo é reorganizar um trabalho acadêmico em uma estrutura mais próxima de um projeto técnico de portfólio, com dados, código, documentação, análise exploratória e interface web.

## Visão geral

Este projeto trabalha com dados da Pesquisa Nacional da Cesta Básica de Alimentos, do DIEESE, analisando:

- preço histórico da cesta básica;
- tempo de trabalho necessário para sua aquisição;
- comparação entre capitais do Sudeste;
- variações em períodos econômicos relevantes;
- apresentação dos resultados em uma interface web acessível.

## Cidades analisadas

- São Paulo
- Rio de Janeiro
- Belo Horizonte
- Vitória

## Tecnologias

- Python
- Pandas
- Plotly
- Jupyter Notebook / Google Colab
- HTML
- Bootstrap
- GitHub Pages

## Estrutura do projeto

- `data/raw/` — dados brutos extraídos do DIEESE
- `data/processed/` — dados tratados e padronizados
- `notebooks/` — notebooks de análise exploratória
- `src/` — scripts Python de processamento e geração de gráficos
- `outputs/charts/` — gráficos gerados
- `outputs/tables/` — tabelas exportadas
- `web/` — interface web do projeto
- `docs/` — artigo e documentação acadêmica
- `requirements.txt` — dependências necessárias para execução do projeto

## Status atual

O projeto está em processo de reorganização técnica.

### Concluído

- [x] Recuperação das bases brutas do DIEESE
- [x] Organização dos arquivos brutos em `data/raw/`
- [x] Criação do pipeline de processamento em Python
- [x] Geração dos datasets tratados em `data/processed/`
- [x] Registro das dependências em `requirements.txt`
- [x] Criação do script de geração de gráficos em `src/generate_charts.py`
- [x] Refatoração inicial do notebook de análise
- [x] Criação da interface web inicial
- [x] Publicação da interface web via GitHub Pages

### Em andamento

- [ ] Refinamento das análises e interpretações finais
- [ ] Organização dos gráficos e tabelas
- [ ] Documentação da metodologia e dos resultados

## Como executar o projeto

Instale as dependências:

`pip install -r requirements.txt`

Execute o processamento dos dados:

`python src/process_data.py`

Gere os gráficos interativos:

`python src/generate_charts.py`

O primeiro script lê os arquivos brutos em `data/raw/` e gera os arquivos tratados em `data/processed/`.

O segundo script utiliza os datasets tratados para gerar os gráficos HTML em `outputs/charts/`.

## Dados

Os dados brutos foram extraídos da base pública da Pesquisa Nacional da Cesta Básica de Alimentos, do DIEESE.

A etapa atual do projeto utiliza arquivos separados por cidade e métrica, que foram padronizados em dois datasets principais:

- `data/processed/horas_trabalho.csv`
- `data/processed/preco_cesta.csv`

Durante o tratamento, linhas de rodapé e observações textuais da exportação original foram removidas. Foi preservado um valor ausente real identificado em `05-2021` para Belo Horizonte.

## Contexto acadêmico

Este projeto foi desenvolvido originalmente como parte de uma Pesquisa Curricular de Graduação, envolvendo análise de dados, Interação Humano-Computador, acessibilidade digital e publicação de informações em interface web.

A versão atual busca transformar o material original em um repositório mais organizado, reprodutível e adequado para apresentação profissional.

## Próximos passos

1. Refatorar o notebook de análise para usar os arquivos tratados
2. Gerar gráficos a partir dos datasets padronizados
3. Integrar os resultados à interface web
4. Publicar a interface via GitHub Pages
5. Documentar os principais resultados e limitações dos dados

## Autor

**Enzo Liutkus Going**

## Observação

Este repositório ainda está em desenvolvimento. A proposta é evoluir o material acadêmico original para um projeto técnico com melhor organização, reprodutibilidade e apresentação.