
from django.shortcuts import render
from .models import Lieu

def accueil(request):
    lieux = Lieu.objects.all()
    return render(request, "index.html", {"lieux": lieux})
    