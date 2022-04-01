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


def search_by_brand(request):
    if request.method == "POST":
        laptops = Laptop.objects.filter(brand=request.POST["brand"])

        if len(laptops) == 0:
            return render(request, "search_results.html", {"found": False})

        context = {"found": True, "laptops": laptops}
        return render(request, "search_results.html", context)

    return render(request, "search_results.html")
