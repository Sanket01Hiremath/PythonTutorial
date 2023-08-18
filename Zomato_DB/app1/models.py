from django.db import models
from datetime import datetime
  
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    desc=models.TextField(max_length=200)
    inventory = models.JSONField()

class User(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=6)
    type=models.CharField(max_length=1,default="C")
    wallet=models.IntegerField()

class Order(models.Model):
    date=datetime.now()
    restaurant=models.OneToOneField(Restaurant,on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    order=models.JSONField()

class Conversation(models.Model):
    user_message = models.TextField()
    chatbot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
