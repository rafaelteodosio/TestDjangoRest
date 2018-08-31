from django.db import models

# Create your models here.

class Car(models.Model):

    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    cor = models.CharField(max_length=200)
    ano = models.IntegerField(default=None)
