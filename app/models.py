
from django.db import models

class Lieu(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    categorie = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    