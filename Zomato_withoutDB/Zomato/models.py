from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    inventory = models.TextField()

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    items = models.TextField()
    is_delivered = models.BooleanField(default=False)
