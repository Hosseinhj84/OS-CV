from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .models import UserProfile

def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        if password != confirm:
            return render(request, "accounts/register.html", {"error": "رمز عبور مطابقت ندارد."})

        if User.objects.filter(username=username).exists():
            return render(request, "accounts/register.html", {"error": "نام کاربری قبلاً وجود دارد."})

        User.objects.create_user(username=username, password=password)
        return redirect("login")

    return render(request, "accounts/register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.last_login_time = timezone.now()
            profile.save()
            return redirect("dashboard")
        else:
            messages.error(request, "نام کاربری یا رمز اشتباه است")
    return render(request, "accounts/login.html")


def dashboard(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, "accounts/dashboard.html", {"profile": profile})
