from django.shortcuts import render

from application.models import Laptop


def main_page(request):
    return render(request, "base_index.html")


def list_laptops(request):
    laptops = Laptop.objects.all()
    list_photos = [laptop.laptopphoto_set.all()[0].url for laptop in laptops]

    data = []

    for i in range(len(laptops)):
        data.append([laptops[i], list_photos[i]])

    return render(request, "laptops_list.html", {"laptops": data})

