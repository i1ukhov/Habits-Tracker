from rest_framework.serializers import ValidationError


class HabitsValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        data = dict(value)
        related = data.get("related_to")
        if data.get("related_to") and data.get("award"):
            raise ValidationError("Заполните либо вознаграждение, либо связанную привычку")
        if data.get("execution_time") > 120:
            raise ValidationError("Время выполнения должно быть не больше 120 секунд")
        if related and not related.get("is_pleasant"):
            raise ValidationError("Связанная привычка должна быть приятной")
        if data.get("is_pleasant") and (data.get("award") or data.get("related_to")):
            raise ValidationError("Нельзя указать вознаграждение или связанную привычку для приятной привычки")
        if data.get("periodicity") > 7:
            raise ValidationError("Периодичность привычки должна быть не реже, чем раз в неделю")
