from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponseBadRequest
from todoapplication.models import Task
from todoapplication.api.serializers import TaskSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def task_list(request):
    user = request.user
    tasks = Task.objects.filter(user_id=user.id)
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
    else:
        return HttpResponseBadRequest(serializer.errors)

    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def task_update(request):
    try:
        task = Task.objects.get(id=request.data['id'])

        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except:
        return HttpResponseBadRequest()

    return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def task_delete(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete()
    except:
        return HttpResponseBadRequest()
    return Response()
