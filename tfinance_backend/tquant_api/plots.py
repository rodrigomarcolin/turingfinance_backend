"""
Este arquivo contém funções para plotar gráficos interativos usando a biblioteca Plotly Express.

O frontend e o backend podem ser gerados a partir dessas funções, possibilitando que os usuários vejam os resultados
desses gráficos em uma interface de usuário, sem a necessidade de escrever código adicional.

Os inputs de cada função devem ser rigorosamente documentados, bem como o seu output.
"""


import plotly.express as px
from plotly.offline import plot
import json, plotly
import pandas as pd


def plot_histogram(df: pd.DataFrame, title: str, nbins: int = 100) -> str:
    """
    Plota um histograma interativo usando a biblioteca Plotly Express.

    Args:
        df (pd.DataFrame): O DataFrame contendo os dados a serem plotados.
        title (str): O título do histograma.
        nbins (int, optional): O número de bins para o histograma. O padrão é 100.

    Returns:
        str: Uma string contendo o JSON que representa o gráfico plotado.
    """
    
    # TODO: refatorar para receber o pd.Series a ser plotado em vez de receber o df, para
    # assim permitir maior flexibilidade.

    fig = px.histogram(df['Adj Close'].pct_change().dropna(), nbins=nbins, title=title)
    plot_div = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return plot_div


def plot_rolling_std(df: pd.DataFrame, title: str) -> str:
    """
    Plota o desvio padrão móvel de uma série temporal usando a biblioteca Plotly Express.

    Args:
        df (pd.DataFrame): O DataFrame contendo os dados a serem plotados.
        title (str): O título do gráfico.

    Returns:
        str: Uma string contendo o JSON que representa o gráfico plotado.
    """

    # TODO: refatorar para receber o pd.Series a ser plotado em vez de receber o df, para
    # assim permitir maior flexibilidade.

    fig = px.line(df['Close'].rolling(90).std(), title=title)
    plot_div = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return plot_div


