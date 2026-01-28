from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    height_cm = fields.IntField(null=True)
    weight_kg = fields.FloatField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    water_logs: fields.ReverseRelation["WaterLog"]
    exercise_logs: fields.ReverseRelation["ExerciseLog"]
    sleep_logs: fields.ReverseRelation["SleepLog"]
    meal_logs: fields.ReverseRelation["MealLog"]

    def __str__(self) -> str:
        return f"{self.name}({self.id})"
