from turtle import update
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    title=models.TextField(null=True,blank=True)
    body=models.TextField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title[0:30]