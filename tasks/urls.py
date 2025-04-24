from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_or_create_tasks),  # This should be the endpoint to create or get tasks
]
