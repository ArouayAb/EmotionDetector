from datetime import date

from PIL import Image
import numpy as np

from first_app.models.models import InferenceModel


class InferenceService:
    def inference(self, image, model, extractor, classes):
        loadedImage = Image.open(image)
        loadedImage = loadedImage.convert("RGB")

        inputs = extractor(loadedImage, return_tensors="pt")
        outputs = model(**inputs)
        predictions = outputs["logits"].softmax(1)
        prediction_array = np.array(predictions.cpu().detach()).squeeze().tolist()
        zipped_array = zip(classes, prediction_array)

        return dict(zipped_array)

    def persistInference(self, inference):
        for key in inference:
            InferenceModel.objects.create(
                emotion_name=key,
                emotion_percentage=inference[key] * 100,
                creation_date=date.today()
            )

        for sad in InferenceModel.sadness_objects.filter(emotion_name__exact='Sadness'):
            print("----------------")
            print(sad.id)
            print(sad.emotion_name)
            print(sad.emotion_percentage)
            print(sad.creation_date)
            print("----------------")
