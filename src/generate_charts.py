from pathlib import Path

import pandas as pd
import plotly.express as px


PROJECT_ROOT = Path(__file__).resolve().parents[1]

PROCESSED_PATH = PROJECT_ROOT / "data" / "processed"
CHARTS_PATH = PROJECT_ROOT / "outputs" / "charts"

PRECOS_PATH = PROCESSED_PATH / "preco_cesta.csv"
HORAS_PATH = PROCESSED_PATH / "horas_trabalho.csv"


def load_data():
    """Carrega os datasets tratados do projeto."""
    precos = pd.read_csv(PRECOS_PATH)
    horas = pd.read_csv(HORAS_PATH)

    precos["data"] = pd.to_datetime(precos["mes_ano"], format="%m-%Y")
    horas["data"] = pd.to_datetime(horas["mes_ano"], format="%m-%Y")

    precos["ano"] = precos["data"].dt.year
    horas["ano"] = horas["data"].dt.year

    horas["horas_decimal"] = horas["valor_minutos"] / 60

    return precos, horas


def generate_price_chart(precos):
    """Gera gráfico de evolução do preço da cesta básica."""
    precos_pos_1995 = precos[precos["ano"] >= 1995].copy()

    fig = px.line(
        precos_pos_1995,
        x="data",
        y="valor_reais",
        color="cidade",
        title="Evolução do preço da cesta básica por cidade (1995–2024)",
        labels={
            "data": "Ano",
            "valor_reais": "Preço da cesta básica (R$)",
            "cidade": "Cidade",
        },
    )

    fig.update_layout(
        xaxis_title="Ano",
        yaxis_title="Preço da cesta básica (R$)",
        legend_title="Cidade",
        hovermode="x unified",
    )

    return fig


def generate_work_hours_chart(horas):
    """Gera gráfico de horas de trabalho necessárias para aquisição da cesta."""
    horas_pos_1995 = horas[horas["ano"] >= 1995].copy()

    fig = px.line(
        horas_pos_1995,
        x="data",
        y="horas_decimal",
        color="cidade",
        title="Horas de trabalho necessárias para aquisição da cesta básica (1995–2024)",
        labels={
            "data": "Ano",
            "horas_decimal": "Horas de trabalho",
            "cidade": "Cidade",
        },
    )

    fig.update_layout(
        xaxis_title="Ano",
        yaxis_title="Horas de trabalho",
        legend_title="Cidade",
        hovermode="x unified",
    )

    return fig


def main():
    """Executa a geração dos gráficos HTML do projeto."""
    CHARTS_PATH.mkdir(parents=True, exist_ok=True)

    precos, horas = load_data()

    fig_preco = generate_price_chart(precos)
    fig_horas = generate_work_hours_chart(horas)

    preco_output = CHARTS_PATH / "preco_cesta_1995_2024.html"
    horas_output = CHARTS_PATH / "horas_trabalho_1995_2024.html"

    fig_preco.write_html(preco_output)
    fig_horas.write_html(horas_output)

    print("Gráficos gerados com sucesso:")
    print(preco_output)
    print(horas_output)


if __name__ == "__main__":
    main()