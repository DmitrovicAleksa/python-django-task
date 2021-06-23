from django.db import models
from django.contrib.auth.models import User


class ToDo(models.Model):
    title = models.CharField(max_length=30)
    priority = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)

# Create your models here.

