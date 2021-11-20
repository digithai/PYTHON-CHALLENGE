from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.

class Cuisine(models.Model):
    name = models.CharField(max_length=100)

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, related_name='display')