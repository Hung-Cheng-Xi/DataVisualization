import plotly.express as px
import pandas as pd
import geopandas as gpd

from plotly.graph_objects import Figure
from app.schema import MapAreaRecord
from shapely.geometry import shape


def _create_continuous_fig(
    df: pd.DataFrame, year: str, zmin: float, zmax: float
) -> Figure:
    fig = px.choropleth(
        df,
        geojson=df.geometry.__geo_interface__,
        locations=df.index,
        color="aging_rate",
        color_continuous_scale="OrRd",
        range_color=(zmin, zmax),
        labels={"aging_rate": "高齡人口比率 (%)"},
        hover_name="Area",
        projection="mercator",
        title=f"{year} 年 高齡人口比率（連續色階）",
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    return fig


def _create_classified_fig(df: pd.DataFrame, year: str) -> Figure:
    df2 = df.copy()
    df2["norm"] = (df2["aging_rate"] / 20).clip(0, 1)
    scale = [[0, "green"], [0.35, "yellow"], [0.7, "orange"], [1, "red"]]
    fig = px.choropleth(
        df2,
        geojson=df2.geometry.__geo_interface__,
        locations=df2.index,
        color="norm",
        color_continuous_scale=scale,
        range_color=(0, 1),
        labels={"norm": "高齡人口比率 (標準化)"},
        hover_name="Area",
        hover_data={"aging_rate": True},
        projection="mercator",
        title=f"{year} 年 高齡人口比率（分級顏色）",
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        margin=dict(l=0, r=0, t=30, b=0),
        coloraxis_colorbar=dict(
            tickvals=[0, 0.35, 0.7, 1], ticktext=["<7%", "7-14%", "14-20%", ">20%"]
        ),
    )
    return fig


def select_map_fig_from_records(
    map_record: dict[str, list[MapAreaRecord]],
    year: str,
    mode: str,
    zmin: float,
    zmax: float,
):
    # 1. 从模型列表摊平成 DataFrame
    df = pd.DataFrame([rec.model_dump() for rec in map_record[year]])
    # 2. 把 GeoJSON dict 转回 Shapely geometry
    df["geometry"] = df["geometry"].apply(lambda g: shape(g) if g else None)
    # 3. 构造 GeoDataFrame
    gdf = gpd.GeoDataFrame(df, geometry="geometry")
    # 4. 以 Area 设索引，并且再把它写回一列
    gdf = gdf.set_index("Area")
    gdf["Area"] = gdf.index

    # 5. 继续调用你原本的绘图函数
    if mode == "continuous":
        return _create_continuous_fig(gdf, year, zmin, zmax)
    else:
        return _create_classified_fig(gdf, year)
