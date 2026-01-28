from tortoise import fields, models


class MealLog(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="meal_logs")
    meal_type = fields.CharField(max_length=20)
    calories = fields.IntField(null=True)
    note = fields.CharField(max_length=200, null=True)
    eaten_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.meal_type} - {self.calories}kcal"
