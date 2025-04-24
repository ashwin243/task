# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_or_create_tasks),  # 👈 this matches /api/
    path('tasks/', views.get_or_create_tasks),
]
