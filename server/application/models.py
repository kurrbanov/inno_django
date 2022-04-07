from django.db import models
from django.contrib.auth.models import User


class Laptop(models.Model):
    BRAND = (
        ('Apple', 'Apple'),
        ('Acer', ' Acer'),
        ('Asus', 'Asus'),
        ('HP', 'HP'),
        ('Lenovo', 'Lenovo'),
        ('Samsung', 'Samsung'),
        ('Xiaomi', 'Xiaomi')
    )

    PROCESSOR = (
        ('Intel', 'Intel'),
        ('AMD', 'AMD'),
        ('Apple', 'Apple'),
        ('Эльбрус', 'Эльбрус'),
        ('Байкал', 'Байкал')
    )

    name = models.CharField(max_length=255, blank=False)
    brand = models.CharField(max_length=20, blank=False, choices=BRAND)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    weight = models.FloatField()
    display = models.DecimalField(max_digits=3, decimal_places=1)
    ram = models.IntegerField()
    processor = models.CharField(max_length=10, choices=PROCESSOR)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    laptop = models.ManyToManyField(Laptop, blank=True)


class LaptopPhoto(models.Model):
    url = models.URLField()
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, blank=False)


class Category(models.Model):
    name = models.CharField(max_length=25)
