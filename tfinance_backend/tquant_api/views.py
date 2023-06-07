from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.request import Request
import yfinance as yf
import plotly.express as px
from plotly.offline import plot
import json, plotly

# Create your views here.
class HistogramView(APIView):
    def get(self, request : Request):
        ticker = request.query_params.get('ticker').strip()
        ini_date = request.query_params.get('ini_date')
        end_date = request.query_params.get('end_date')

        if (any([not ticker, not ini_date, not end_date])) or len(ticker.strip()) < 4:
            return Response("Insira as informações necessárias!", status=status.HTTP_400_BAD_REQUEST)
        
        df = yf.download(ticker, start=ini_date, end=end_date)
        fig = px.histogram(df['Adj Close'].pct_change().dropna(), nbins=100, title='Histograma de Retornos Diários')
        
        plot_div = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        return Response({'hist': plot_div})