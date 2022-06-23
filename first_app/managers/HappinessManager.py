from django.db import models


class HappinessManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(emotion_name='Happiness')
