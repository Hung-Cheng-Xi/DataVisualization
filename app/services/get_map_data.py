from app.schema import FunnelRecord
from app.services.parse.parse_map_excel import parse_map_data


def get_map_data() -> list[FunnelRecord]:
    """
    取得地圖圖表所需的資料
    """
    geo_filename = "twCounty2010.geo.json"
    excel_filename = "人口比率.xlsx"
    return parse_map_data(geo_filename, excel_filename)
