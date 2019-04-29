from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import TaskList,Task
from api.serializers import TaskListSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def task_list (request):
    if request.method == 'GET':
        tasklists = TaskList.objects.all()
        serializer = TaskListSerializer(tasklists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status.HTTP_500_INTERNAL_SERVER_ERROR )

@api_view(['GET' , 'PUT', 'DELETE'])
def task_list_actions (request,pk):
    try :
        tl = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TaskListSerializer(tl)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer (instance=tl, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status.HTTP_500_INTERNAL_SERVER_ERROR )
    elif request.method == 'DELETE':
        tl.delete()
        return Response("DELETED!!!!!!")
