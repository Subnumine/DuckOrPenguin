from django.db import models

class Animals(models.Model):
    name = models.fields.CharField(max_length=100)

class ImageAnimals(models.Model):
    image = models.ImageField()