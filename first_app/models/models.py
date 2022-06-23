from django.db import models

from first_app.managers.AngerManager import AngerManager
from first_app.managers.ContemptManager import ContemptManager
from first_app.managers.DisgustManager import DisgustManager
from first_app.managers.FearManager import FearManager
from first_app.managers.HappinessManager import HappinessManager
from first_app.managers.NeutralManager import NeutralManager
from first_app.managers.SadnessManager import SadnessManager


# Create your models here.
from first_app.managers.SurpriseManager import SurpriseManager


class InferenceModel(models.Model):
    emotion_name = models.CharField(max_length=15)
    emotion_percentage = models.DecimalField(max_digits=7, decimal_places=4)
    creation_date = models.DateField()

    # managers / daos
    objects = models.Manager()

    sadness_objects = SadnessManager()
    anger_objects = AngerManager()
    contempt_objects = ContemptManager()
    disgust_objects = DisgustManager()
    fear_objects = FearManager()
    neutral_objects = NeutralManager()
    surprise_objects = SurpriseManager()
    happiness_objects = HappinessManager()
