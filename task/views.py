from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView

from .models import Task
from .forms import TaskForm


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



class TaskView(APIView):
    def delete(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def list(self, request):
        tasks = Task.objects.all()
        search = request.GET.get('search', '')
        if search:
            tasks = tasks.filter(title__icontains=search)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)