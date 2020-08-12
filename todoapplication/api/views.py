from rest_framework.decorators import api_view
from rest_framework.response import Response

from todoapplication.models import Task

from todoapplication.api.serializers import TaskSerializer


@api_view(['GET'])
def api_get_all_tasks(request):
    tasks = Task.objects.get()
    serializer = TaskSerializer(tasks)

    return Response(serializer.data)
