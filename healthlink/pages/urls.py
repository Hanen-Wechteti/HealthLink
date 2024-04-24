from django.urls import path

from .  import views

ulrspatterns = [
    path('', views.index, name='index')
]