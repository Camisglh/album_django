from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PhotoForm
from .models import Category, Photo
from .tasks import process_photo


def cached_query(query, key, timeout=None):
    """
    Cache the results of a query to improve performance.
    """
    cached_results = cache.get(key)

    if cached_results is not None:
        return cached_results

    results = query()
    cache.set(key, results, timeout=timeout)

    return results


def home(request, category_slug=None):
    """
    Display the home page with photos and categories.
    """

    def get_photos():
        if category_slug:
            current_category = Category.objects.get(slug=category_slug)
            return Photo.objects.filter(category=current_category)
        else:
            return Photo.objects.all()

    def get_categories():
        return Category.objects.all()

    cached_photos = cached_query(get_photos, "home_photos", timeout=300)
    categories = cached_query(get_categories, "home_categories")

    if category_slug:
        current_category = Category.objects.get(slug=category_slug)
    else:
        current_category = None

    return render(
        request,
        "home.html",
        {
            "photos": cached_photos,
            "categories": categories,
            "current_category": current_category,
            "category_slug": category_slug,
        },
    )


@login_required
def add_photo(request):
    """
    Add a new photo.
    """
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            process_photo.delay(photo.id)
            return redirect("card:home")
    else:
        form = PhotoForm()

    return render(request, "add_photo.html", {"form": form})


@login_required
def edit_photo(request, photo_id):
    """
    Edit an existing photo.
    """
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
    """
    Delete a photo.
    """

    def get_photo():
        photo = get_object_or_404(Photo, id=photo_id, user=request.user)
        return photo

    cached_photo = cached_query(get_photo, "delete_photo_photo", timeout=300)

    if request.method == "POST":
        photo = cached_photo
        photo.delete()
        return redirect("user:profile")

    return render(request, "delete_photo.html", {"photo": cached_photo})
