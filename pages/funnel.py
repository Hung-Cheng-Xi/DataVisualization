# pages/funnel_page.py

import dash
from dash import Input, Output, html, dcc
from chart.funnel import get_funnel_figs_from_records
from services import (
    parse_funnel_excel,
    get_funnel_chart_records,
)

dash.register_page(__name__, path="/funnel", name="人口金字塔")

records_by_year = parse_funnel_excel(filename="三年人數統計.xlsx")
records = get_funnel_chart_records(records_by_year)

figs = get_funnel_figs_from_records(records)
selected_years = ["103-完整版", "108-完整版", "113-完整版"]
year_map = {
    "103-完整版": [y for y in figs if y.startswith("103")],
    "108-完整版": [y for y in figs if y.startswith("108")],
    "113-完整版": [y for y in figs if y.startswith("113")],
}

layout = html.Div(
    [
        html.H2("三年人口金字塔", style={"textAlign": "center", "margin": "1rem"}),
        dcc.Tabs(
            id="funnel-tabs",
            value="103-完整版",
            children=[dcc.Tab(label=f"{y}", value=y) for y in selected_years],
            style={"margin": "0 2rem"},
        ),
        html.Div(id="funnel-content", style={"padding": "1rem"}),
    ]
)


@dash.callback(Output("funnel-content", "children"), Input("funnel-tabs", "value"))
def render_funnel(tab_value):
    keys = year_map[tab_value]
    fig = figs[keys[0]]
    return dcc.Graph(figure=fig, config={"responsive": True}, style={"height": "70vh"})
