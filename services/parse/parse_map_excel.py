import os
import pandas as pd
import geopandas as gpd

from schema import MapAreaRecord


def _get_mnt_data_path(filename: str) -> str:
    """
    取得 mnt/data 資料夾下的檔案路徑
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "..", "mnt", "data", filename)


def parse_map_data(
    geojson_filename: str,
    excel_filename: str,
    sheet_names: tuple[str, str, str] = ("113", "108", "103"),
) -> tuple[dict[str, pd.DataFrame], float, float]:
    """
    讀取地圖資料和人口比率 Excel 檔案，並回傳各年度的地圖區域記錄。
    """

    geojson_path = _get_mnt_data_path(geojson_filename)
    excel_path = _get_mnt_data_path(excel_filename)

    gdf = gpd.read_file(geojson_path)
    gdf["Area"] = gdf["COUNTYNAME"].astype(str).str.strip().str.replace("台", "臺")
    gdf = gdf.drop(columns=["COUNTYNAME"])

    def _clean(df: pd.DataFrame) -> pd.DataFrame:
        df = df.rename(columns={"區域別": "Area", "高齡人口比率": "aging_rate"})
        df["Area"] = df["Area"].astype(str).str.strip().str.replace("台", "臺")
        return df

    df113 = _clean(pd.read_excel(excel_path, sheet_name=sheet_names[0]))
    df108 = _clean(pd.read_excel(excel_path, sheet_name=sheet_names[1]))
    df103 = _clean(pd.read_excel(excel_path, sheet_name=sheet_names[2]))

    merged = {
        "113": gdf.merge(df113, on="Area", how="left"),
        "108": gdf.merge(df108, on="Area", how="left"),
        "103": gdf.merge(df103, on="Area", how="left"),
    }
    combined = pd.concat([m["aging_rate"] for m in merged.values()])
    zmin, zmax = combined.min(), combined.max()

    # convert to list of Pydantic models
    records_dict: dict[str, list[MapAreaRecord]] = {}
    for year, df_year in merged.items():
        records: list[MapAreaRecord] = []
        for _, row in df_year.iterrows():
            geom = None
            if hasattr(row.geometry, "__geo_interface__"):
                geom = row.geometry.__geo_interface__
            records.append(
                MapAreaRecord(
                    Area=row["Area"],
                    aging_rate=float(row["aging_rate"])
                    if pd.notna(row["aging_rate"])
                    else None,
                    geometry=geom,
                )
            )
        records_dict[year] = records

    return records_dict, float(zmin), float(zmax)
