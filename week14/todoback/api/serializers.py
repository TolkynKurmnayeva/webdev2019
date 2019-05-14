from api.models import Task, TaskList
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    created_at = serializers.DateTimeField()
    due_on = serializers.DateTimeField()
    status = serializers.CharField()
    tasklist_id = serializers.IntegerField()

    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status', 'tasklist_id')

class TaskSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    created_at = serializers.DateTimeField()
    due_on = serializers.DateTimeField()
    status = serializers.CharField()

    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status')


class TaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    owner = UserSerializer(read_only=True)
    tasks = TaskSerializer2(many=True)

    class Meta:
        model = TaskList
        fields = ('id', 'name', 'owner', 'tasks')

    def create(self, validated_data):
        tasks = validated_data.pop('tasks')
        tasklist = TaskList.objects.create(**validated_data)
        for t in tasks:
            Task.objects.create(tasklist=tasklist, **t)
        return tasklist
