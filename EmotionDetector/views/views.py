import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from EmotionDetector.config.apps import EmotionDetectorConfig

from EmotionDetector.services.InferenceService import InferenceService


class AnalysisView(TemplateView):
    template_name = "EmotionDetector/analysis.html"

    def get(self, request, **kwargs):
        return render(request, self.template_name, None)


class LandingView(TemplateView):
    landing_page = "EmotionDetector/index.html"

    def get(self, request, **kwargs):
        return render(request, self.landing_page, None)

