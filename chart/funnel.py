from typing import list
import pandas as pd
import plotly.express as px

from general import parse_age_label
from services.calculate_funnel_service import FunnelRecord


def show_funnel_chart_from_records(funnel_records: list[FunnelRecord]):
    """
    接受 FunnelRecord 列表，並繪製各年度的漏斗金字塔圖
    """
    # 轉為 DataFrame
    df = pd.DataFrame([rec.model_dump() for rec in funnel_records])

    for year in df["year"].unique():
        df_year = df[df["year"] == year]
        sorted_ages = sorted(df_year["age_group"].unique(), key=parse_age_label)
        # 反轉排列：底部 0 歲，頂部 100+
        category_order = sorted_ages[::-1]

        fig = px.funnel(
            df_year,
            x="total",
            y="age_group",
            color="sex",
            orientation="h",
            title=f"{year} 年人口金字塔",
        )
        fig.update_layout(
            yaxis={"categoryorder": "array", "categoryarray": category_order},
            xaxis_title="人口數（人）",
            yaxis_title="年齡層",
        )
        fig.show()
