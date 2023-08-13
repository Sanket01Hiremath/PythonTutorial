from typing import Any
from django.db import models
from django.db.models import JSONField
  
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    desc=models.TextField(max_length=200)
    inventory = models.JSONField()
    order =models.JSONField()


class User(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=6)
    order=models.JSONField()
    wallet=models.IntegerField()

