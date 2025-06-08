import plotly.express as px

df = px.data.stocks()
fig = px.line(df, x="date", y="GOOG")

fig.update_xaxes(minor=dict(ticks="inside", showgrid=True))

fig.show()
