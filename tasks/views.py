from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

# tasks/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TaskListView(APIView):
    def get(self, request):
        # Example response (fetch data from your model, etc.)
        data = [
            {"id": 1, "name": "Task 1", "completed": False},
            {"id": 2, "name": "Task 2", "completed": True}
        ]
        return Response(data, status=status.HTTP_200_OK)

def task_list(request):
    return JsonResponse({'tasks': []})
