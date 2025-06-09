import dash
from dash import html, dcc

from chart import get_life_line_fig_from_records
from services import get_life_line_data


dash.register_page(__name__, path="/life-line", name="出生死亡線圖")


def layout():
    records = get_life_line_data()
    fig = get_life_line_fig_from_records(records)

    return html.Div(
        [
            html.H2(
                "出生和死亡統計", style={"textAlign": "center", "marginTop": "1rem"}
            ),
            dcc.Graph(
                id="life-line-graph",
                figure=fig,
                config={"responsive": True},
                style={"height": "70vh"},
            ),
        ]
    )
