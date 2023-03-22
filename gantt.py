import plotly.express as px
import plotly
import pandas as pd


df = pd.read_excel('Tasks.xlsx')

tasks = df['tasks']
start = df['Start']
finish = df['finish']
complete = df['Complete in %']

# Create gantt Chart
fig = px.timeline(df, x_start=start, x_end=finish, y=tasks,
                  color=complete, title='Taskks Overview')

# update/change layout
fig.update_yaxes(autorange='reversed')
fig.update_layout(
    title_font_size=42,
    font_size=18,
    title_font_family='Arial'
)
# interact button in chart
fig = ff.create_gantt(df)

# save in HTML
plotly.offline.plot(fig, filename='task_overview.html')
