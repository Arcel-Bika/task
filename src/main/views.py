from django.shortcuts import render, get_object_or_404
from main.models import Task


def task(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task(title=title, description=description)
        task.save()
    return render(request, 'create_task.html')


def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return render(request, 'task_list.html', {'tasks': Task.objects.all()})
