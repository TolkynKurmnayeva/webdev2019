from api.models import Task, TaskList
from rest_framework import serializers
from django.contrib.auth.models import User



class TaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = TaskList
        fields = ('id', 'name')

class TaskSerializer (serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    created_at = serializers.CharField()
    status = serializers.CharField()
    due_on = serializers.CharField()
    taskList = TaskListSerializer()

    class Meta:
        model = Task
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ('id', 'username', 'email')
