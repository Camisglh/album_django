from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import PhotoForm
from .models import Category, Photo


def home(request, category_slug=None):
    if category_slug:
        current_category = Category.objects.get(slug=category_slug)
        photos = Photo.objects.filter(category=current_category)
    else:
        current_category = None
        photos = Photo.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        "home.html",
        {
            "photos": photos,
            "categories": categories,
            "current_category": current_category,
            "category_slug": category_slug,
        },
    )


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
