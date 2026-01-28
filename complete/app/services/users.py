from app.models.user import User

DEFAULT_USER_NAME = "학생"


async def get_or_create_default_user() -> User:
    user = await User.first()
    if user:
        return user
    return await User.create(name=DEFAULT_USER_NAME, height_cm=170, weight_kg=65.0)
