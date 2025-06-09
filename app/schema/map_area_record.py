from pydantic import BaseModel


class MapAreaRecord(BaseModel):
    Area: str
    aging_rate: float
    geometry: dict
