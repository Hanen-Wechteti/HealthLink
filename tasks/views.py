from django.shortcuts import render


def index(request):
    return render(request, 'tasks/tasks.html')

def task(request):
    return render(request, 'tasks/task.html')

def search(request):
    return render(request, 'tasks/search.html')
