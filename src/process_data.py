import re
from pathlib import Path

import pandas as pd


RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")

PROCESSED_PATH.mkdir(parents=True, exist_ok=True)


def is_valid_month_year(value):
    value = str(value).strip()
    return bool(re.match(r"^\d{2}-\d{4}$", value))


def time_to_minutes(value):
    if pd.isna(value):
        return None

    value = str(value).replace("\r", "").strip()

    match = re.match(r"^(\d+)h(\d+)m$", value)
    if not match:
        return None

    hours = int(match.group(1))
    minutes = int(match.group(2))

    return hours * 60 + minutes


def clean_currency(value):
    if pd.isna(value):
        return None

    value = str(value).replace("\r", "").strip()

    if value == "" or value.lower() == "nan":
        return None

    value = value.replace("R$", "").replace(" ", "")

    if "," in value and "." in value:
        value = value.replace(".", "").replace(",", ".")
    elif "," in value:
        value = value.replace(",", ".")

    try:
        return float(value)
    except ValueError:
        return None


def load_dieese_file(file_name, city, metric):
    path = RAW_PATH / file_name

    df = pd.read_excel(path)

    df = df.iloc[1:].reset_index(drop=True)
    df = df.rename(columns={
        df.columns[0]: "mes_ano",
        df.columns[1]: "valor_original"
    })

    df["mes_ano"] = df["mes_ano"].astype(str).str.strip()

    # Mantém apenas linhas reais de dados no formato MM-AAAA
    df = df[df["mes_ano"].apply(is_valid_month_year)].copy()

    # Limpa valor original sem perder nulos reais
    df["valor_original"] = df["valor_original"].apply(
        lambda x: None if pd.isna(x) else str(x).replace("\r", "").strip()
    )

    df["cidade"] = city
    df["metrica"] = metric

    if metric == "horas_trabalho":
        df["valor_minutos"] = df["valor_original"].apply(time_to_minutes)
    elif metric == "preco_cesta":
        df["valor_reais"] = df["valor_original"].apply(clean_currency)

    return df


def process_hours():
    files = [
        ("horas_sp.xls", "São Paulo"),
        ("horas_bh.xls", "Belo Horizonte"),
        ("horas_rj.xls", "Rio de Janeiro"),
        ("horas_vitoria.xls", "Vitória"),
    ]

    dfs = [
        load_dieese_file(file_name, city, "horas_trabalho")
        for file_name, city in files
    ]

    df = pd.concat(dfs, ignore_index=True)
    df.to_csv(PROCESSED_PATH / "horas_trabalho.csv", index=False, encoding="utf-8-sig")

    return df


def process_prices():
    files = [
        ("preco_sp.xls", "São Paulo"),
        ("preco_bh.xls", "Belo Horizonte"),
        ("preco_rj.xls", "Rio de Janeiro"),
        ("preco_vitoria.xls", "Vitória"),
    ]

    dfs = [
        load_dieese_file(file_name, city, "preco_cesta")
        for file_name, city in files
    ]

    df = pd.concat(dfs, ignore_index=True)
    df.to_csv(PROCESSED_PATH / "preco_cesta.csv", index=False, encoding="utf-8-sig")

    return df


def main():
    hours_df = process_hours()
    prices_df = process_prices()

    print("Dados processados com sucesso.")
    print(f"horas_trabalho.csv: {len(hours_df)} linhas")
    print(f"preco_cesta.csv: {len(prices_df)} linhas")

    print("\nValores ausentes em horas:")
    print(hours_df[hours_df["valor_minutos"].isna()][["mes_ano", "cidade", "valor_original"]])

    print("\nValores ausentes em preços:")
    print(prices_df[prices_df["valor_reais"].isna()][["mes_ano", "cidade", "valor_original"]])


if __name__ == "__main__":
    main()