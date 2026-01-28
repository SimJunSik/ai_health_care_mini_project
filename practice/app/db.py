from pathlib import Path

from tortoise import Tortoise

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "health.db"
DB_URL = f"sqlite://{DB_PATH}"


async def init_db() -> None:
    await Tortoise.init(
        db_url=DB_URL,
        modules={
            "models": [
                "app.models.user",
                "app.models.water",
                # TODO: Exercise/Sleep/Meal 모델을 추가하세요.
            ]
        },
    )
    await Tortoise.generate_schemas()


async def close_db() -> None:
    await Tortoise.close_connections()
