from plotly import graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Funnel(
        name="Montreal",
        y=[
            "Website visit",
            "Downloads",
            "Potential customers",
            "Requested price",
            "invoice sent",
        ],
        x=[120, 60, 40, 30, 20],
        textinfo="value+percent initial",
    )
)

fig.add_trace(
    go.Funnel(
        name="Toronto",
        orientation="h",
        y=[
            "Website visit",
            "Downloads",
            "Potential customers",
            "Requested price",
            "invoice sent",
        ],
        x=[100, 60, 40, 30, 20],
        textposition="inside",
        textinfo="value+percent previous",
    )
)

fig.show()
