import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from first_app.config.apps import FirstAppConfig

from first_app.services.InferenceService import InferenceService


class InferenceView(TemplateView):
    template_name = "first_app/Upload.html"
    inference_service = InferenceService()

    def get(self, request, **kwargs):
        context = {'name': 'Hello from noob'}
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        input_image = request.FILES["file"]

        results = self.inference_service.inference(
            input_image,
            FirstAppConfig.model,
            FirstAppConfig.extractor,
            FirstAppConfig.classes
        )

        self.inference_service.persistInference(results)

        return HttpResponse(json.dumps(results))