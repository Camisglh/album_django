from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
    return render(request, "auth/register.html", {"form": form})


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
    return render(request, "auth/login.html", {"error_message": error_message})


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def profile(request):
    user_photos = Photo.objects.filter(user=request.user)
    return render(request, "auth/profile.html", {"user_photos": user_photos})
