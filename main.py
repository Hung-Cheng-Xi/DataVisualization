from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)
app.title = "資料可視化 - 台灣人口變遷與高齡化趨勢"

app.layout = html.Div(
    [
        html.Header(
            html.H1("台灣人口變遷與高齡化趨勢"),
            style={"textAlign": "center", "padding": "1rem"},
        ),
        html.Nav(
            [
                dcc.Link(page["name"], href=page["path"], style={"margin": "0 1rem"})
                for page in dash.page_registry.values()
            ],
            style={
                "textAlign": "center",
                "backgroundColor": "#eee",
                "padding": "0.5rem",
            },
        ),
        dash.page_container,
    ]
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
