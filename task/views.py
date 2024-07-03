from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response



from .models import Task
from .forms import TaskForm
from .serializers import TaskSerializer


@login_required
def task_list(request):
    tasks = Task.objects.all().order_by('due_date')
    context = {
        'in_progress': tasks.filter(status='In Progress'),
        'completed': tasks.filter(status='Completed'),
        'overdue': tasks.filter(status='Overdue'),
    }
    return render(request, 'task/task_list.html', context)


@login_required
def get_all_tasks(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request, 'task/all_tasks.html', {'tasks': tasks})

@login_required
def create_task(request):
    users = get_user_model().objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
        else:
            return render(request, 'task/create_task.html', {'form': form, 'users': users, 'errors': form.errors})
    else:
        form = TaskForm()
    return render(request, 'task/create_task.html', {'form': form, 'users': users})



@login_required
def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    users = get_user_model().objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
        else:
            return render(request, 'task/get_task.html', {'form': form, 'task': task, 'users': users, 'errors': form.errors})


@login_required
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:task_list')
    else:
        return render(request, 'task/get_task.html', {'task': task})


@login_required
def get_task(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'task/get_task.html', {'task': task})

@login_required
def get_users(request):
    users = get_user_model().objects.all()
    return render(request, 'task/list_users.html', {'users': users})


class ListTaskView(APIView):

    def get(self, request):
        tasks = Task.objects.all()
        search = request.GET.get('search', '')
        sort = request.GET.get('sort', 'due_date')
        
        if sort:
            if sort not in ['priority', 'due_date', 'status']:
                sort = 'due_date'
            tasks = tasks.order_by(sort)
        
        if search:
            tasks = tasks.filter(title__icontains=search)
        
        
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)