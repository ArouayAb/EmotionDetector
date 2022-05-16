from django.urls import path
from . import views

app_name = 'first_app'
urlpatterns = [
    path('upload', views.UploadView.as_view(), name='upload'),
    path('', views.LandingView.as_view(), name='landing'),
]
