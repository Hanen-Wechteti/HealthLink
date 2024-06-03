from django.shortcuts import render
from django.http import HttpResponse
from tasks.choices import care_choices, city_choices, state_choices

from tasks.models import Task
from nurses.models import Nurse

def index(request):
    tasks = Task.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = { 
        'tasks': tasks,
        'care_choices':care_choices,
        'city_choices':city_choices,
        'state-choices':state_choices
        }

    return render(request,'pages/index.html', context)

def about(request):
    nurses = Nurse.objects.order_by('-hire_date')

    mvp_nurses = Nurse.objects.all().filter(is_mvp=True)
    context = { 
        'nurses': nurses,
        'mvp_nurses': mvp_nurses
        }

    return render(request,'pages/about.html')