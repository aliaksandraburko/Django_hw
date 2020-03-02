from django.db import models


# Create your models here.

class Patient(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

