from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

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


@login_required
def edit_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id, user=request.user)

    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect("user:profile")
    else:
        form = PhotoForm(instance=photo)

    return render(request, "edit_photo.html", {"form": form})


@login_required
def delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id, user=request.user)

    if request.method == "POST":
        photo.delete()
        return redirect("user:profile")

    return render(request, "delete_photo.html", {"photo": photo})
