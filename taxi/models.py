from django.db import models

class Taxi(models.Model):
    name = models.CharField(max_length=50)
    plate = models.CharField(max_length=50)
    driver = models.CharField(max_length=100, unique=True)
    passenger = models.CharField(max_length=100)
    model = models.CharField(max_length=25)
    statsu = models.CharField(max_length=50)
