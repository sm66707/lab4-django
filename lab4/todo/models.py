from turtle import update
from django.db import models

class Todo(models.Model):
    name = models.fields.CharField(verbose_name="Todo Name", max_length=100)#, unique=True)
    priority = models.fields.IntegerField(verbose_name="Todo Priority", default=1)
    todo_date = models.fields.DateTimeField(verbose_name="Todo Date", default='2019-01-01 10:10') 
    is_done = models.fields.BooleanField(verbose_name="Todo Done", default=False)
    description = models.fields.TextField(verbose_name="Todo Description", default='', max_length=500)
    creation_time = models.fields.DateTimeField(verbose_name="Creation Time",auto_now_add=True)
    update_time = models.fields.DateTimeField(verbose_name="Update Time", auto_now=True)

    def __str__(self):
        return f"Todo: {self.name} At Time: {self.creation_time}"

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
        ordering = ['-id']

class Task(models.Model):
    name = models.fields.CharField(verbose_name="Task Name", max_length=100)
    todo = models.ForeignKey('todo', on_delete=models.CASCADE)#on_delete=models.SET_NULL, null=True)

# class Actor(models.Model):
#     pass

# class Movie(models.Model):
#     actors = models.ManyToManyField('actor')
#     directors = models.ManyToManyField('director')
#     serial_number = models.OneToOneField('serial_number', on_delete=models.CASCADE)

# class Director(models.Model):
#     pass

# class serial(models.Model):
#     pass