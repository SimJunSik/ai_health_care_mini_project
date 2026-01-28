from tortoise import fields, models


class SleepLog(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="sleep_logs")
    sleep_date = fields.DateField()
    start_time = fields.DatetimeField()
    end_time = fields.DatetimeField()
    quality = fields.IntField(null=True)

    def __str__(self) -> str:
        return f"{self.sleep_date} - q{self.quality}"
