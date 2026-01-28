from datetime import date, datetime

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


class ExerciseCreate(BaseModel):
    user_id: int
    activity: str
    duration_min: int
    calories_burned: int | None = None


class ExerciseOut(BaseModel):
    id: int
    user_id: int
    activity: str
    duration_min: int
    calories_burned: int | None
    logged_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SleepCreate(BaseModel):
    user_id: int
    sleep_date: date
    start_time: datetime
    end_time: datetime
    quality: int | None = None


class SleepOut(BaseModel):
    id: int
    user_id: int
    sleep_date: date
    start_time: datetime
    end_time: datetime
    quality: int | None

    model_config = ConfigDict(from_attributes=True)


class MealCreate(BaseModel):
    user_id: int
    meal_type: str
    calories: int | None = None
    note: str | None = None


class MealOut(BaseModel):
    id: int
    user_id: int
    meal_type: str
    calories: int | None
    note: str | None
    eaten_at: datetime

    model_config = ConfigDict(from_attributes=True)
