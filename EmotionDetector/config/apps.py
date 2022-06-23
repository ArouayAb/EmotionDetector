from django.apps import AppConfig
from transformers import AutoFeatureExtractor, AutoModelForImageClassification


class EmotionDetectorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EmotionDetector'

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


