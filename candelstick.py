import pandas_datareader as web
from datetime import datetime
import pandas as pd
import plotly.graph_objs as go
import plotly


# Get Stock Data
start = datetime(2020, 1, 1)
end = datetime(2020, 7, 31)
stock = 'TSLA'
df = web.DataReader(stock, 'yahoo', start, end)
df = df.reset_index()

# making candelstick
fig = go.Figure(data=[go.Candlestick(
    x=df['Data'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Adj Close']
)])

# exporting Candlestick to HTML
plotly.offline.plot(fig, filename='Candlestick.html')
