import pandas as pd
from app.schema import LifeLineRecord
import plotly.express as px
from plotly.graph_objects import Figure
from typing import List


def get_life_line_fig_from_records(
    life_line_records: List[LifeLineRecord],
) -> Figure:
    """
    接受 LifeRecord 列表，回傳 Plotly Figure。
    """
    df = pd.DataFrame([rec.model_dump() for rec in life_line_records])

    df = df.rename(
        columns={
            "year": "年份",
            "births": "出生總數",
            "deaths": "死亡總數",
            "natural_change": "自然增減",
        }
    )
    x_col = "年份"
    y_cols = ["出生總數", "死亡總數", "自然增減"]
    labels = {
        "年份": "年份（民國）",
        "value": "人數（人）",
        "variable": "指標",
        "出生總數": "出生總數",
        "死亡總數": "死亡總數",
        "自然增減": "自然增減",
    }
    title = "民國103年至113年 出生與死亡人數比較"

    # Plot line chart
    fig = px.line(df, x=x_col, y=y_cols, markers=True, labels=labels, title=title)
    fig.update_layout(
        legend_title_text=labels.get("variable"),
        xaxis=dict(dtick=1),
        margin={"l": 40, "r": 20, "t": 50, "b": 20},
    )

    return fig
