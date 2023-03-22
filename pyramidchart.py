import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv(r"C:\Users\karti\Desktop\India-2020.csv")
y = df['Age']
x1 = df['M']
x2 = df['F']

fig = go.Figure()

fig.add_trace(go.Bar(
    y=y,
    x=x2,
    name='Female',
    orientation='h'
))

fig.update_layout(
    template='plotly_white',
    title='Age Pyramid Indian 2020 ',
    title_font_size=24,
    barmode='relative',
    bargap=0.0,
    bagroupgap=0,
    xaxis=dict(
        tickvals=[-4000000, -2000000, 0, 2000000, 4000000],
        ticktext=['4M', '2M', '0', '2M', '4M'],
        title='Population in Mio',
        title_font_size=14
    )
)

fig.show()
