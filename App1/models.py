from django.db import models
# Acá creamos los modelos necesarios con sus atributos, elegimos dos por cada clase.
class Artist(models.Model):
    name=models.CharField(max_length=40)
    nacionality=models.CharField(max_length=40)
    biography = models.TextField()
    img = models.ImageField(null=True, blank=True) #Agregamos imagenes!
    def __str__(self):
        return f"Name: {self.name} - Nacionality: {self.nacionality}"

class Label(models.Model):
    name=models.CharField(max_length=40)
    country=models.CharField(max_length=40)
    description= models.TextField()
    img = models.ImageField(null=True, blank=True)
    def __str__(self):
        return f"Name: {self.name} - Country: {self.country}"


class Instrument(models.Model):
    name=models.CharField(max_length=40)
    type=models.CharField(max_length=40)
    description= models.TextField()
    img = models.ImageField(null=True, blank=True)
    def __str__(self):
        return f"Name: {self.name} - Type: {self.type}"
class Genre(models.Model):
    name=models.CharField(max_length=40)
    country_of_origin=models.CharField(max_length=40)
    description= models.TextField()
    img = models.ImageField(null=True, blank=True)
    def __str__(self):
        return f"Name: {self.name} - Country of origin: {self.country_of_origin}"
    
class aboutMe(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=1500)
    img = models.ImageField(null=True, blank=True)
    def __str__(self):
        return f"Name: {self.name} - Descrition: {self.description}"

