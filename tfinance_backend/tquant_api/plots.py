import plotly.express as px
from plotly.offline import plot
import json, plotly


def plot_histogram(df, title, nbins=100):
    fig = px.histogram(df['Adj Close'].pct_change().dropna(), nbins=nbins, title=title)
    plot_div = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return plot_div

def plot_rolling_std(df, title):
    fig = px.line(df['Close'].rolling(90).std(), title=title)
    plot_div = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return plot_div