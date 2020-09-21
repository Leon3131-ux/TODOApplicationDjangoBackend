from django.urls import path

from todoapplication.api import views

app_name = 'todoapplication'

urlpatterns = [
    path('tasks', views.task_list, name="tasks"),
    path('createTask', views.task_create, name="taskCreate"),
    path('saveTask', views.task_update, name="taskUpdate"),
    path('deleteTask', views.task_delete, name="taskDelete")
]
