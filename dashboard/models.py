from gc import is_finalized
from tabnanny import verbose
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    
# This function returns the title
    def __str__(self):
        return self.title

# BY DEFAULT DJANGO ADDS AN EXTRA 'S' to componets in the admin ,
# this class helps to remove that. 
    class Meta:
        verbose_name="notes"
        verbose_name_plural="notes"


class Homework(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    description=models.TextField()
    due=models.DateTimeField()
    is_finished=models.BooleanField(default=False)
    def __str__(self):
        return self.title


class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    is_finished=models.BooleanField(default=False)
    def __str__(self):
        return self.title
