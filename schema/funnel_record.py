from pydantic import BaseModel, Field


class FunnelRecord(BaseModel):
    year: str = Field(..., description="年度")
    age_group: str = Field(..., description="年齡層")
    sex: str = Field(..., description="性別 (男/女)")
    total: int = Field(..., description="該年齡層性別人口總數")
