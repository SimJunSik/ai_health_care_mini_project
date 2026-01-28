from tortoise import fields, models


class WaterLog(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="water_logs")
    amount_ml = fields.IntField()
    logged_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user_id} - {self.amount_ml}ml"
