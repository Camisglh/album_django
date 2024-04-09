from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import PhotoForm
from .models import Photo


def home(request):
    photos = Photo.objects.all()
    return render(request, "home.html", {"photos": photos})


@login_required
def add_photo(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect("card:home")
    else:
        form = PhotoForm()
    return render(request, "add_photo.html", {"form": form})
