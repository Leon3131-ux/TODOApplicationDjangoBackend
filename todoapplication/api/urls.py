from django.urls import path

from todoapplication.api.views import api_get_all_tasks

app_name = 'todoapplication'

urlpatterns = [
    path('getTasks', api_get_all_tasks, name="tasks")
]
