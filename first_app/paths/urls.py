from django.urls import path

from first_app.views import views, InferenceView

app_name = 'first_app'
urlpatterns = [
    path('analysis', views.AnalysisView.as_view(), name='analysis'),
    path('upload', InferenceView.InferenceView.as_view(), name='upload'),
    path('', views.LandingView.as_view(), name='landing'),
]
