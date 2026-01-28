from fastapi import APIRouter

from app.models.exercise import ExerciseLog
from app.models.meal import MealLog
from app.models.sleep import SleepLog
from app.models.water import WaterLog
from app.schemas import (
    ExerciseCreate,
    ExerciseOut,
    MealCreate,
    MealOut,
    SleepCreate,
    SleepOut,
    WaterCreate,
    WaterOut,
)

router = APIRouter()


@router.get("/water", response_model=list[WaterOut])
async def list_water():
    logs = await WaterLog.all().order_by("-logged_at")
    return [WaterOut.model_validate(log) for log in logs]


@router.post("/water", response_model=WaterOut)
async def create_water(payload: WaterCreate):
    log = await WaterLog.create(user_id=payload.user_id, amount_ml=payload.amount_ml)
    return WaterOut.model_validate(log)


@router.get("/exercise", response_model=list[ExerciseOut])
async def list_exercise():
    logs = await ExerciseLog.all().order_by("-logged_at")
    return [ExerciseOut.model_validate(log) for log in logs]


@router.post("/exercise", response_model=ExerciseOut)
async def create_exercise(payload: ExerciseCreate):
    log = await ExerciseLog.create(
        user_id=payload.user_id,
        activity=payload.activity,
        duration_min=payload.duration_min,
        calories_burned=payload.calories_burned,
    )
    return ExerciseOut.model_validate(log)


@router.get("/sleep", response_model=list[SleepOut])
async def list_sleep():
    logs = await SleepLog.all().order_by("-sleep_date")
    return [SleepOut.model_validate(log) for log in logs]


@router.post("/sleep", response_model=SleepOut)
async def create_sleep(payload: SleepCreate):
    log = await SleepLog.create(
        user_id=payload.user_id,
        sleep_date=payload.sleep_date,
        start_time=payload.start_time,
        end_time=payload.end_time,
        quality=payload.quality,
    )
    return SleepOut.model_validate(log)


@router.get("/meal", response_model=list[MealOut])
async def list_meal():
    logs = await MealLog.all().order_by("-eaten_at")
    return [MealOut.model_validate(log) for log in logs]


@router.post("/meal", response_model=MealOut)
async def create_meal(payload: MealCreate):
    log = await MealLog.create(
        user_id=payload.user_id,
        meal_type=payload.meal_type,
        calories=payload.calories,
        note=payload.note,
    )
    return MealOut.model_validate(log)
