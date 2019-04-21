from api.models import Task, TaskList
from rest_framework import serializers


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ('id', 'name')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ('id', 'name', 'created_at', 'due_on', 'status')

