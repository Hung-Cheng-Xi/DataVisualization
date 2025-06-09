from app.until import parse_age_label
from app.schema import FunnelRecord


def get_funnel_chart_records(records_by_year: dict[str, list]) -> list[FunnelRecord]:
    """
    解析原始 RegionAgeRecord 產生適用於漏斗圖的人口金字塔資料列表
    """
    funnel_records: list[FunnelRecord] = []
    for year, recs in records_by_year.items():
        male_counts: dict[str, int] = {}
        female_counts: dict[str, int] = {}
        for rec in recs:
            target = male_counts if rec.sex == "男" else female_counts
            for age, count in rec.age_groups.items():
                target[age] = target.get(age, 0) + count

        # 依數字排序年齡層
        all_ages = sorted(set(male_counts) | set(female_counts), key=parse_age_label)
        for age in all_ages:
            funnel_records.append(
                FunnelRecord(
                    year=year, age_group=age, sex="男", total=male_counts.get(age, 0)
                )
            )
            funnel_records.append(
                FunnelRecord(
                    year=year, age_group=age, sex="女", total=female_counts.get(age, 0)
                )
            )
    return funnel_records
