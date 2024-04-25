from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/', views.task, name='task'),
    path('search/', views.search, name='search'),
]
