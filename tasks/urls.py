from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>', views.task, name='task'),
    path('search/', views.search, name='search'),
]
