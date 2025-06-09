from pydantic import BaseModel


class LifeLineRecord(BaseModel):
    year: int
    deaths: int
    births: int
    natural_change: int
