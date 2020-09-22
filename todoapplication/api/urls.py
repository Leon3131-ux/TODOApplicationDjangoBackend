from django.urls import path

from todoapplication.api import views

app_name = 'todoapplication'

urlpatterns = [
    path('tasks', views.task_list, name="tasks"),
    path('saveTask', views.task_save, name="taskCreate"),
    path('updateTask', views.task_update, name="taskUpdate"),
    path('deleteTask/<int:pk>', views.task_delete, name="taskDelete"),
    path('login', views.MyTokenObtainPairView.as_view(), name="login")
]
