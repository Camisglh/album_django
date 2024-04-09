from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import UserCreationForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("")
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
            return redirect("")
        else:
            error_message = "Неверный логин или пароль"
    else:
        error_message = None
    return render(request, "auth/login.html", {"error_message": error_message})
