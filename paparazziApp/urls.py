from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('famosos', views.famosos),
    path('videos', views.videos)
]