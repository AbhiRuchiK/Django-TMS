from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import UserCreateForm, UserLoginForm


def login_view(request):
    next = request.GET.get("next")
    form = UserLoginForm(request.POST or None)
    if "login" in request.POST:
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            if next:
                return redirect(next)

            context = {"username": username}
            return render(request, "task_management_system_home.html", context)
    context = {"form": form}
    return render(request, "login.html", context)


def create_account_view(request):
    next = request.GET.get("next")
    form = UserCreateForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")
    context = {"form": form}
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login_account"))
