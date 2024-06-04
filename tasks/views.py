from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Task
from tasks.choices import care_choices, city_choices, state_choices

def index(request):
    tasks = Task.objects.order_by('-list_date').filter(is_published=True)
    
    paginator = Paginator(tasks, 6)  # Utilisez Paginator avec une majuscule
    page = request.GET.get('page')
    paged_tasks = paginator.get_page(page)

    context = {
        'tasks': paged_tasks
    }
    return render(request, 'tasks/tasks.html', context)

def task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context = {
        'task': task  # Utilisez une clé singulière pour une tâche individuelle
    }
    return render(request, 'tasks/task.html', context)

def search(request):
    queryset_list = Task.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Care needs
    if 'care' in request.GET:
        care = request.GET['care']
        if care:
            queryset_list = queryset_list.filter(care__icontains=care)

    context = { 
        'care_choices': care_choices,
        'city_choices': city_choices,
        'state_choices': state_choices,
        'tasks': queryset_list,
        'values': request.GET
    }

    return render(request, 'tasks/search.html', context)
