from pydantic import BaseModel


class RegionAgeRecord(BaseModel):
    area: str
    sex: str
    year: str
    total: int
    age_groups: dict[str, int]
