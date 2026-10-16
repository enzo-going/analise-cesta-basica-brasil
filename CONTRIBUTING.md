# Contribuindo

Pull requests são bem-vindos. Para mudanças grandes, abra uma issue antes para
discutir o que você pretende alterar.

Antes de abrir o PR, rode o mesmo que o CI roda:

```bash
pip install -r requirements.txt
ruff check .
python src/process_data.py
git diff --exit-code -- data/processed
python src/generate_charts.py
git diff --exit-code -- outputs/charts
```

Os dois `git diff` são a checagem de reprodutibilidade: os CSVs de
`data/processed` e os gráficos de `outputs/charts` são versionados e precisam
sair idênticos da geração. Se a mudança altera números ou gráficos de propósito,
faça commit dos arquivos gerados no mesmo PR.
