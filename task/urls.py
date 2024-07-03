from django.urls import path
from .views import (
    task_list, create_task, 
    get_task, delete_task, 
    update_task, get_users, 
    get_all_tasks, ListTaskView)


app_name = "tasks"
urlpatterns = [
    path('list/', task_list, name='task_list'),
    path('all-tasks/', get_all_tasks, name='all_tasks'),
    path('create/', create_task, name='create_task'),
    path('users/', get_users, name='task_users'),
    path('detail/<str:pk>', get_task, name='get_task'),
    path('update/<str:pk>', update_task, name='update_task'),
    path('delete/<str:pk>', delete_task, name='delete_task'),
    path('api/tasks', ListTaskView.as_view(), name="task-api")
]
