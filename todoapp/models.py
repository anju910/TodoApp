from django.db import models


class Completed(models.Model):
    completed=models.CharField(max_length=10,unique=True)
    def __str__(self):
        return self.completed

class ToDoCreate(models.Model):
    task_name=models.CharField(max_length=30)
    completed=models.ForeignKey(Completed,on_delete=models.CASCADE,null=True)
    created_by=models.CharField(max_length=25)

    def __str__(self):
        return self.task_name