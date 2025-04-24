from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list),  # or whatever your view is
]
