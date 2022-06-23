from django.db import models

from EmotionDetector.managers.AngerManager import AngerManager
from EmotionDetector.managers.ContemptManager import ContemptManager
from EmotionDetector.managers.DisgustManager import DisgustManager
from EmotionDetector.managers.FearManager import FearManager
from EmotionDetector.managers.HappinessManager import HappinessManager
from EmotionDetector.managers.NeutralManager import NeutralManager
from EmotionDetector.managers.SadnessManager import SadnessManager


# Create your models here.
from EmotionDetector.managers.SurpriseManager import SurpriseManager


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
