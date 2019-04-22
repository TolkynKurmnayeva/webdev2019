from django.shortcuts import render
from api.models import Task, TaskList
from django.http import  HttpResponse,JsonResponse


# Create your views here.
def task_list (request) :
    tasks = TaskList.objects.all()
    json_tasks = [m.to_json() for m in tasks]
    return JsonResponse (json_tasks, safe=False)

def task_detail (request, pk):
    taskList = TaskList.objects.get(id=pk)
    tasks=taskList.task_set.all()
    json_tasks = [t.to_json() for t in tasks]
    return JsonResponse(json_tasks, safe=False)

def task_get (request, pk):
    taskLists = TaskList.objects.all()
    tasks = []
    for i in range(pk):
        tasks.append(taskLists[i])
    json_tasks = [t.to_json() for t in tasks]
    return JsonResponse(json_tasks, safe=False)

