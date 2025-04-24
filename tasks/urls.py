# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_or_create_tasks),  # Make sure this matches the URL being requested
]
