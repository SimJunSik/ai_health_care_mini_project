from tortoise import fields, models


class ExerciseLog(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="exercise_logs")
    activity = fields.CharField(max_length=100)
    duration_min = fields.IntField()
    calories_burned = fields.IntField(null=True)
    logged_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.activity}({self.duration_min}m)"
