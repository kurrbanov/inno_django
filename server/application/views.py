from django.shortcuts import render
from django.contrib import messages

from application.models import Laptop, Cart
from application.form import RegistrationUser


def main_page(request):
    return render(request, "base_index.html")


def list_laptops(request):
    laptops = Laptop.objects.all()
    list_photos = [laptop.laptopphoto_set.all()[0].url for laptop in laptops]

    data = []

    for i in range(len(laptops)):
        data.append([laptops[i], list_photos[i]])

    return render(request, "laptops_list.html", {"laptops": data})


def search_by_brand(request):
    if request.method == "POST":
        laptops = Laptop.objects.filter(brand=request.POST["brand"])

        if len(laptops) == 0:
            return render(request, "search_results.html", {"found": False})

        context = {"found": True, "laptops": laptops}
        return render(request, "search_results.html", context)

    return render(request, "search_results.html")


def registration(request):
    form = RegistrationUser()

    if request.method == "POST":
        form = RegistrationUser(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_cart = Cart(user=new_user)
            new_user.save()
            new_cart.save()
        else:
            messages.error(request, "Форма регистрации заполнена неверно!")
            return render(request, "registration.html")

    return render(request, "registration.html", {"form": form})
