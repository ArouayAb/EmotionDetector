from django.urls import path

from EmotionDetector.views import views, InferenceView

app_name = 'EmotionDetector'
urlpatterns = [
    path('analysis', views.AnalysisView.as_view(), name='analysis'),
    path('upload', InferenceView.InferenceView.as_view(), name='upload'),
    path('', views.LandingView.as_view(), name='landing'),
]
