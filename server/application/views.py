from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from application.models import Laptop, Cart
from application.form import RegistrationUser


def registration(request):
    if request.user.is_authenticated:
        return redirect('')

    form = RegistrationUser()

    if request.method == "POST":
        form = RegistrationUser(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_cart = Cart(user=new_user)
            new_user.save()
            new_cart.save()
            return redirect('')
        else:
            messages.error(request, "Форма регистрации заполнена неверно!")
            return render(request, "registration.html")

    return render(request, "registration.html", {"form": form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("")
        else:
            messages.error(request, "Неверный логин или пароль!")

    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect('')


def main_page(request):
    a = 1 / 0
    return render(request, "base_index.html")


def laptops(request):
    laptops_ = Laptop.objects.all()
    list_photos = [laptop.laptopphoto_set.all()[0].url for laptop in laptops_]

    data = []

    for i in range(len(laptops_)):
        data.append([laptops_[i], list_photos[i]])

    return render(request, "laptops_list.html", {"laptops": data})


def search(request):
    if request.method == "POST":
        laptops_ = Laptop.objects.filter(brand=request.POST["brand"])

        if len(laptops_) == 0:
            return render(request, "search_results.html", {"found": False})

        context = {"found": True, "laptops": laptops_}
        return render(request, "search_results.html", context)

    return render(request, "search_results.html")
