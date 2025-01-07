
from django.db import models
from app.models import Lieu

class Avis(models.Model):
    utilisateur = models.CharField(max_length=255)
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)
    commentaire = models.TextField()
    note = models.IntegerField()
    