from datetime import date, datetime
from pathlib import Path

from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import matplotlib
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from app.models.exercise import ExerciseLog
from app.models.meal import MealLog
from app.models.sleep import SleepLog
from app.models.water import WaterLog
from app.services.users import get_or_create_default_user

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def build_water_report(logs: list[WaterLog], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not logs:
        plt.figure(figsize=(7, 3.5))
        plt.text(0.5, 0.5, "데이터 없음", ha="center", va="center", fontsize=12)
        plt.axis("off")
        plt.tight_layout()
        plt.savefig(output_path, dpi=140)
        plt.close()
        return

    rows = [{"date": log.logged_at.date(), "amount_ml": log.amount_ml} for log in logs]
    df = pd.DataFrame(rows)
    daily = df.groupby("date", as_index=False)["amount_ml"].sum()

    plt.figure(figsize=(7, 3.5))
    plt.bar(daily["date"].astype(str), daily["amount_ml"], color="#6e7bff")
    plt.title("일별 수분 섭취량")
    plt.ylabel("ml")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path, dpi=140)
    plt.close()


@router.get("/")
async def dashboard(request: Request):
    user = await get_or_create_default_user()
    water_logs = await WaterLog.filter(user=user).order_by("-logged_at").limit(5)
    exercise_logs = await ExerciseLog.filter(user=user).order_by("-logged_at").limit(5)
    sleep_logs = await SleepLog.filter(user=user).order_by("-sleep_date").limit(5)
    meal_logs = await MealLog.filter(user=user).order_by("-eaten_at").limit(5)

    total_water = sum([log.amount_ml for log in await WaterLog.filter(user=user)])
    total_exercise = sum([log.duration_min for log in await ExerciseLog.filter(user=user)])

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "user": user,
            "water_logs": water_logs,
            "exercise_logs": exercise_logs,
            "sleep_logs": sleep_logs,
            "meal_logs": meal_logs,
            "total_water": total_water,
            "total_exercise": total_exercise,
        },
    )


@router.get("/water")
async def water_page(request: Request):
    user = await get_or_create_default_user()
    logs = await WaterLog.filter(user=user).order_by("-logged_at")
    return templates.TemplateResponse(
        "water.html", {"request": request, "user": user, "logs": logs}
    )


@router.post("/water")
async def add_water(amount_ml: int = Form(...)):
    user = await get_or_create_default_user()
    await WaterLog.create(user=user, amount_ml=amount_ml)
    return RedirectResponse(url="/water", status_code=303)


@router.get("/exercise")
async def exercise_page(request: Request):
    user = await get_or_create_default_user()
    logs = await ExerciseLog.filter(user=user).order_by("-logged_at")
    return templates.TemplateResponse(
        "exercise.html", {"request": request, "user": user, "logs": logs}
    )


@router.post("/exercise")
async def add_exercise(
    activity: str = Form(...),
    duration_min: int = Form(...),
    calories_burned: int | None = Form(None),
):
    user = await get_or_create_default_user()
    await ExerciseLog.create(
        user=user,
        activity=activity,
        duration_min=duration_min,
        calories_burned=calories_burned,
    )
    return RedirectResponse(url="/exercise", status_code=303)


@router.get("/sleep")
async def sleep_page(request: Request):
    user = await get_or_create_default_user()
    logs = await SleepLog.filter(user=user).order_by("-sleep_date")
    return templates.TemplateResponse(
        "sleep.html", {"request": request, "user": user, "logs": logs}
    )


@router.post("/sleep")
async def add_sleep(
    sleep_date: str = Form(...),
    start_time: str = Form(...),
    end_time: str = Form(...),
    quality: int | None = Form(None),
):
    user = await get_or_create_default_user()
    await SleepLog.create(
        user=user,
        sleep_date=date.fromisoformat(sleep_date),
        start_time=datetime.fromisoformat(start_time),
        end_time=datetime.fromisoformat(end_time),
        quality=quality,
    )
    return RedirectResponse(url="/sleep", status_code=303)


@router.get("/meal")
async def meal_page(request: Request):
    user = await get_or_create_default_user()
    logs = await MealLog.filter(user=user).order_by("-eaten_at")
    return templates.TemplateResponse(
        "meal.html", {"request": request, "user": user, "logs": logs}
    )


@router.post("/meal")
async def add_meal(
    meal_type: str = Form(...),
    calories: int | None = Form(None),
    note: str | None = Form(None),
):
    user = await get_or_create_default_user()
    await MealLog.create(user=user, meal_type=meal_type, calories=calories, note=note)
    return RedirectResponse(url="/meal", status_code=303)


@router.get("/report")
async def report_page(request: Request):
    user = await get_or_create_default_user()
    logs = await WaterLog.filter(user=user).order_by("logged_at")
    output_path = Path("app/static/img/water_report.png")
    build_water_report(logs, output_path)
    total_water = sum(log.amount_ml for log in logs)
    days = len({log.logged_at.date() for log in logs})
    avg_per_day = round(total_water / days, 1) if days else 0

    return templates.TemplateResponse(
        "report.html",
        {
            "request": request,
            "user": user,
            "chart_url": "/static/img/water_report.png",
            "total_water": total_water,
            "days": days,
            "avg_per_day": avg_per_day,
        },
    )
