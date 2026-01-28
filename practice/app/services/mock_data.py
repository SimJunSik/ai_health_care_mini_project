from datetime import date, datetime

# TODO: 아래 in-memory 데이터는 ORM으로 교체하는 과제입니다.

_exercise_logs = [
    {"activity": "러닝", "duration_min": 30, "calories_burned": 260, "logged_at": datetime.now()},
    {"activity": "요가", "duration_min": 45, "calories_burned": 180, "logged_at": datetime.now()},
]

_sleep_logs = [
    {
        "sleep_date": date.today(),
        "start_time": datetime.now(),
        "end_time": datetime.now(),
        "quality": 4,
    }
]

_meal_logs = [
    {"meal_type": "아침", "calories": 420, "note": "그릭요거트", "eaten_at": datetime.now()}
]


def list_exercise():
    return _exercise_logs


def add_exercise(activity: str, duration_min: int, calories_burned: int | None):
    _exercise_logs.insert(
        0,
        {
            "activity": activity,
            "duration_min": duration_min,
            "calories_burned": calories_burned,
            "logged_at": datetime.now(),
        },
    )


def list_sleep():
    return _sleep_logs


def add_sleep(sleep_date: date, start_time: datetime, end_time: datetime, quality: int | None):
    _sleep_logs.insert(
        0,
        {
            "sleep_date": sleep_date,
            "start_time": start_time,
            "end_time": end_time,
            "quality": quality,
        },
    )


def list_meal():
    return _meal_logs


def add_meal(meal_type: str, calories: int | None, note: str | None):
    _meal_logs.insert(
        0,
        {
            "meal_type": meal_type,
            "calories": calories,
            "note": note,
            "eaten_at": datetime.now(),
        },
    )
