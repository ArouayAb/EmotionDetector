from django.apps import AppConfig
from transformers import AutoFeatureExtractor, AutoModelForImageClassification


class FirstAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'first_app'

    extractor = AutoFeatureExtractor.from_pretrained("Rajaram1996/FacialEmoRecog")
    model = AutoModelForImageClassification.from_pretrained("Rajaram1996/FacialEmoRecog")
    classes = [
        "Anger",
        "Contempt",
        "Disgust",
        "Fear",
        "Happiness",
        "Neutral",
        "Sadness",
        "Surprise"
    ]


