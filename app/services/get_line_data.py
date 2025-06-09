from app.schema import FunnelRecord
from .calculate.calculate_line_service import get_life_records


def get_life_line_data() -> list[FunnelRecord]:
    """
    取得生命線圖所需的資料，包含出生、死亡、自然增長等數據
    """
    return get_life_records()
