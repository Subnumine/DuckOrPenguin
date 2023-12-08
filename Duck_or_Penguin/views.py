# ~/projects/django-web-app/merchex/listings/views.py
from django.shortcuts import render, redirect
from Duck_or_Penguin.models import *
from .forms import *
from Duck_or_Penguin.Detection import detection
import tensorflow as tf
import os

def home(request):
    return render(request, 'Duck_or_Penguin/hello.html')

def duck(request):
    animal = Animals.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            photo = ImageAnimals.objects.last()
            reponse = detection(photo.image.url[1:])
            if (reponse==22) | (reponse==62):
                return render(request, 'Duck_or_Penguin/canard.html', {'animal': animal[int(reponse)], 
                                                                'photo':photo})
            else:
                return render(request, 'Duck_or_Penguin/meh.html', {'animal': animal[int(reponse)], 
                                                            'photo':photo})
    else:
        form = ImageForm()
        ImageAnimals.objects.all().delete()
    return render(request, 'Duck_or_Penguin/hello.html', {'form': form})