
from django.shortcuts import render, redirect
from .forms import AvisForm

def ajouter_avis(request, lieu_id):
    if request.method == "POST":
        form = AvisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accueil")
    