import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from first_app.config.apps import FirstAppConfig

from first_app.services.InferenceService import InferenceService


class AnalysisView(TemplateView):
    template_name = "first_app/analysis.html"

    def get(self, request, **kwargs):
        return render(request, self.template_name, None)


class LandingView(TemplateView):
    landing_page = "first_app/index.html"

    def get(self, request, **kwargs):
        return render(request, self.landing_page, None)

