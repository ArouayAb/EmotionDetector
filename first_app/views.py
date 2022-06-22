import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .apps import FirstAppConfig
from PIL import Image
import numpy as np


class AnalysisView(TemplateView):
    template_name = "first_app/analysis.html"

    def get(self, request, **kwargs):
        return render(request, self.template_name, None)


class LandingView(TemplateView):
    landing_page = "first_app/index.html"

    def get(self, request, **kwargs):
        return render(request, self.landing_page, None)


class UploadView(TemplateView):
    template_name = "first_app/Upload.html"

    def get(self, request, **kwargs):
        context = {'name': 'Hello from noob'}
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        input_image = request.FILES["file"]
        results = inference(input_image, FirstAppConfig.model, FirstAppConfig.extractor, FirstAppConfig.classes)
        return HttpResponse(json.dumps(results))


def inference(image, model, extractor, classes):
    loadedImage = Image.open(image)
    loadedImage = loadedImage.convert("RGB")

    inputs = extractor(loadedImage, return_tensors="pt")
    outputs = model(**inputs)
    predictions = outputs["logits"].softmax(1)
    prediction_array = np.array(predictions.cpu().detach()).squeeze().tolist()
    zipped_array = zip(classes, prediction_array)

    return dict(zipped_array)
