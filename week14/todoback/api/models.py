from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TaskManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)


class TaskList (models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = TaskManager()

    def __str__(self):
        return self.name


class Task (models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    due_on = models.DateTimeField()
    status = models.CharField(max_length=200)
    tasklist = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name

