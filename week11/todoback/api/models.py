from django.db import models

# Create your models here.

class TaskList (models.Model):
    name = models.CharField(max_length=200)
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name

        }

    def __str__(self):
        return self.name

class Task ( models.Model ) :
    name = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200, default='recently')
    due_on = models.CharField(max_length=200, default='soon')
    status = models.CharField(max_length=200)
    TaskList = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status

        }