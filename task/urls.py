from django.urls import path
from .views import task_list, create_task


app_name = "tasks"
urlpatterns = [
    path('list/', task_list, name='task_list'),
    path('create/', create_task, name='create_task'),
]
