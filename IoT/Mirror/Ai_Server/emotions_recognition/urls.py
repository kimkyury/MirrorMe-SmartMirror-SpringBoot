from django.urls import path
from . import views

urlpatterns = [
    path('findemotion/', views.findEmotion, name='emotion'),
]