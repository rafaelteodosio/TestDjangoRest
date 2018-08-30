from django.db import models

# Create your models here.

class Car(models.Model):

    marca = CharField(max_length=200)
    modelo = CharField(max_length=200)
    cor = CharField(max_length=200)
    ano = IntegerField(default=None)
