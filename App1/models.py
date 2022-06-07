from django.db import models

# Acá creamos los modelos necesarios con sus atributos, elegimos dos por cada clase.
class Artist(models.Model):
    name=models.CharField(max_length=40)
    nacionality=models.CharField(max_length=40)

class Label(models.Model):
    name=models.CharField(max_length=40)
    country=models.CharField(max_length=40)

class Instrument(models.Model):
    name=models.CharField(max_length=40)
    type=models.CharField(max_length=40)

class Genre(models.Model):
    name=models.CharField(max_length=40)
    country_of_origin=models.CharField(max_length=40)

    