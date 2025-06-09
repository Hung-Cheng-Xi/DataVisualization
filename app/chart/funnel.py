import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure
from app.until import parse_age_label
from app.schema import FunnelRecord


def get_funnel_figs_from_records(
    funnel_records: list[FunnelRecord],
) -> dict[str, Figure]:
    """
    接受 FunnelRecord 列表，
    回傳一個 dict: { year_str: Figure }
    """
    df = pd.DataFrame([rec.model_dump() for rec in funnel_records])

    figs: dict[str, Figure] = {}
    for year in sorted(df["year"].unique()):
        df_year = df[df["year"] == year]
        # 年齡層從大到小排（頂端最大齡、底端最小齡）
        sorted_ages = sorted(df_year["age_group"].unique(), key=parse_age_label)[::-1]

        fig = px.funnel(
            df_year,
            x="total",
            y="age_group",
            color="sex",
            orientation="h",
            title=f"{year} 年人口金字塔",
            labels={"total": "人口數（人）", "age_group": "年齡層"},
        )
        fig.update_layout(
            yaxis={"categoryorder": "array", "categoryarray": sorted_ages},
            margin={"l": 40, "r": 20, "t": 50, "b": 20},
        )
        figs[year] = fig

    return figs
