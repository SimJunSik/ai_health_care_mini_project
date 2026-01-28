from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WaterCreate(BaseModel):
    user_id: int
    amount_ml: int


class WaterOut(BaseModel):
    id: int
    user_id: int
    amount_ml: int
    logged_at: datetime

    model_config = ConfigDict(from_attributes=True)
