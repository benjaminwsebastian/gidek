from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
    ProfileImageUpdateForm,
)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            if form.cleaned_data.get("agreed"):
                username = form.cleaned_data.get("username")
                messages.info(request, "Account created, please sign in")
                return redirect("login")

    form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})