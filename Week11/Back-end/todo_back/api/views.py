from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from api.models import TaskList,Task

def index(request):
    return HttpResponse('<h1>What is your main focuse for today?<h1>')

def tasklists(request):
    task_list = TaskList.objects.all()
    json_tasks = [a.to_json() for a in task_list]
    return JsonResponse(json_tasks, safe=False)

def task_detail(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(task_list.to_json())

def tasks(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks = task_list.task_set.all()
    json_task = [a.to_json() for a in tasks]
    return JsonResponse(json_task, safe=False)