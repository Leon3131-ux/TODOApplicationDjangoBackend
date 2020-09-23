from rest_framework.decorators import api_view, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.http import Http404
from todoapplication.models import Task
from todoapplication.api.serializers import TaskSerializer, get_validation_errors, MyTokenObtainPairSerializer
from rest_framework import status
from todoapplication.decorators import group_required


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@group_required(['TaskUser'])
def task_list(request):
    user = request.user
    tasks = Task.objects.filter(user_id=user.id)
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@group_required(['TaskUser'])
def task_save(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
    else:
        return Response({'validationErrors': get_validation_errors(serializer.errors)},
                        status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@group_required(['TaskUser'])
def task_update(request):
    try:
        task = Task.objects.get(id=request.data['id'])
    except Task.DoesNotExist:
        raise Http404()

    if task.user != request.user:
        return Response(status=status.HTTP_403_FORBIDDEN)

    serializer = TaskSerializer(instance=task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({'validationErrors': get_validation_errors(serializer.errors)},
                        status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@group_required(['TaskUser'])
def task_delete(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        raise Http404()

    if task.user != request.user:
        return Response(status=status.HTTP_403_FORBIDDEN)

    if not task.deleted:
        task.deleted = True
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    task.delete()
    return Response()


