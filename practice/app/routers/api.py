from fastapi import APIRouter

from app.models.water import WaterLog
from app.schemas import WaterCreate, WaterOut

router = APIRouter()


@router.get("/water", response_model=list[WaterOut])
async def list_water():
    logs = await WaterLog.all().order_by("-logged_at")
    return [WaterOut.model_validate(log) for log in logs]


@router.post("/water", response_model=WaterOut)
async def create_water(payload: WaterCreate):
    log = await WaterLog.create(user_id=payload.user_id, amount_ml=payload.amount_ml)
    return WaterOut.model_validate(log)


# TODO: Exercise/Sleep/Meal API를 추가해 보세요.
