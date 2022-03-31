from django.db import models


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
