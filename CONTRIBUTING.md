# Contribuindo

Pull requests são bem-vindos. Para mudanças grandes, abra uma issue antes para
discutir o que você pretende alterar.

Antes de abrir o PR, rode o mesmo que o CI roda:

```bash
pip install -r requirements.txt
ruff check .
python src/process_data.py
git diff --exit-code -- data/processed
```

O último comando é a checagem de reprodutibilidade: os CSVs de `data/processed`
são versionados e precisam sair idênticos do reprocessamento dos dados brutos.
Se a mudança altera esses números de propósito, faça commit dos CSVs gerados no
mesmo PR.
