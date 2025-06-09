from app.schema import FunnelRecord
from app.services.calculate.calculate_funnel_service import get_funnel_chart_records
from app.services.parse import parse_funnel_excel


def get_funnel_data() -> list[FunnelRecord]:
    """
    取得漏斗圖所需的資料
    """
    filename = "三年人數統計.xlsx"
    records_by_year = parse_funnel_excel(filename=filename)
    return get_funnel_chart_records(records_by_year=records_by_year)
