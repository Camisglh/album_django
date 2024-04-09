from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import redirect, render

from card.models import Photo

from .forms import UserCreationForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("card:home")
    else:
        form = UserCreationForm()

    register_form = cache.get("register_form")
    if register_form is None:
        register_form = form
        cache.set("register_form", register_form, 60)

    return render(request, "auth/register.html", {"form": register_form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("card:home")
        else:
            error_message = "Неверный логин или пароль"
    else:
        error_message = None

    login_template = cache.get("login_template")
    if login_template is None:
        login_template = render(
            request, "auth/login.html", {"error_message": error_message}
        )
        cache.set("login_template", login_template, 60)

    return login_template


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def profile(request):
    user_photos = cache.get("user_photos_%s" % request.user.id)
    if user_photos is None:
        user_photos = Photo.objects.filter(user=request.user)
        cache.set("user_photos_%s" % request.user.id, user_photos, 60)

    return render(request, "auth/profile.html", {"user_photos": user_photos})
