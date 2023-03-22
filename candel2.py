import pandas_datareader as web
from datetime import datetime
import pandas as pd
import plotly.graph_objs as go
import plotly
import sys
import os
os.chdir(sys.path[0])

# Get Stock Data
start = datetime(2020, 1, 1)
end = datetime(2020, 7, 31)
stock = 'TSLA'
df = web.DataReader(stock, 'yahoo', start, end)
df = df.reset_index()

# Create Candlestick
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Adj Close']
)])

# // Black Background and no gridlines
# fig.update_layout(plot_bgcolor='rgb(0,0,0)',
#                     xaxis =  {'showgrid': False},
#                     yaxis =  {'showgrid': False})

# Export Candlestick to HTML
plotly.offline.plot(fig, filename='Candlestick.html')
