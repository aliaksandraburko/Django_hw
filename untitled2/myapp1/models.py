from django.db import models


# Create your models here.

class Customer(models.Model):
    firstname = models.CharField(max_length=255, default=None)
    lastname = models.CharField(max_length=255, default=None)
    age = models.IntegerField()
