from django.db import models

class Meals(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField()
    price = models.TextField()
    cuisine = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)


