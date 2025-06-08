from chart import show_funnel_chart_from_records
from services import (
    read_region_age_records_by_year,
    get_funnel_chart_records,
)


def _get_mnt_data_path(filename: str) -> str:
    import os

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "EndTerm", "mnt", "data", filename)


if __name__ == "__main__":
    filename = "三年人數統計.xlsx"
    path = _get_mnt_data_path(filename=filename)
    records_by_year = read_region_age_records_by_year(path=path)

    # show funnel chart data
    df_agg = get_funnel_chart_records(records_by_year)
    show_funnel_chart_from_records(df_agg)
