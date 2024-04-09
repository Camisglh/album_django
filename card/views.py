from django.shortcuts import render

from .models import Photo


def home(request):
    photos = Photo.objects.all()
    return render(request, "home.html", {"photos": photos})
