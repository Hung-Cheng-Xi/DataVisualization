import dash
from dash import html, dcc, Input, Output

from chart import select_map_fig_from_records
from services.get_map_data import get_map_data


dash.register_page(__name__, path="/", name="台灣高齡人口地圖")

data_dict, ZMIN, ZMAX = get_map_data()


def layout():
    return html.Div(
        [
            html.H2(
                "台灣高齡人口地圖", style={"textAlign": "center", "marginTop": "1rem"}
            ),
            dcc.RadioItems(
                id="color-mode",
                options=[
                    {"label": "連續色階", "value": "continuous"},
                    {"label": "分級顏色", "value": "classified"},
                ],
                value="continuous",
                inline=True,
                style={"textAlign": "center", "marginBottom": "1rem"},
            ),
            dcc.Tabs(
                id="tabs",
                value="113",
                children=[
                    dcc.Tab(label=f"{y}年", value=y) for y in ["113", "108", "103"]
                ],
            ),
            html.Div(id="tab-content", style={"height": "80vh", "overflow": "auto"}),
        ]
    )


@dash.callback(
    Output("tab-content", "children"),
    Input("tabs", "value"),
    Input("color-mode", "value"),
)
def render_map(tab, mode):
    fig = select_map_fig_from_records(data_dict, tab, mode, ZMIN, ZMAX)
    return dcc.Graph(figure=fig, config={"responsive": True}, style={"height": "100%"})
