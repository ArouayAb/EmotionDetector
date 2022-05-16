import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .apps import FirstAppConfig
from PIL import Image
import numpy as np


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
        context = {}
        results = inference(input_image, FirstAppConfig.model, FirstAppConfig.extractor, FirstAppConfig.classes)
        context["results"] = results
        return HttpResponse(json.dumps(context))


def inference(image, model, extractor, classes):
    loadedImage = Image.open(image)
    loadedImage = loadedImage.convert("RGB")

    inputs = extractor(loadedImage, return_tensors="pt")
    outputs = model(**inputs)
    predictions = outputs["logits"].softmax(1)
    prediction_array = np.array(predictions.cpu().detach()).squeeze().tolist()
    zipped_array = zip(classes, prediction_array)

    print(zipped_array)

    empty = {}
    for i in zipped_array:
        empty[i[0]] = i[1]

    a = sorted(empty.items(), key=lambda x: x[1], reverse=True)
    a = a[:5]
    total = sum([j for i, j in a])
    a = [(i, j / total) for i, j in a]

    # results = dict(a)

    return a
