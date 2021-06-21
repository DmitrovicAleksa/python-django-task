from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User


class ToDo(models.Model):
    title = models.CharField(max_length=30)
    priority = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Create your models here.
