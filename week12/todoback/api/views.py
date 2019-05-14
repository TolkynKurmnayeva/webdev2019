from django.shortcuts import render
from api.models import Task, TaskList
from django.http import  HttpResponse,JsonResponse
from api.serializers import TaskListSerializer, TaskSerializer
from rest_framework import  viewsets

# Create your views here.
class TaskListViewSet (viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

class TaskViewSet (viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



