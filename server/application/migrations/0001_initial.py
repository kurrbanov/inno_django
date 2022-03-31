# Generated by Django 4.0.3 on 2022-03-31 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(choices=[('Apple', 'Apple'), ('Acer', ' Acer'), ('Asus', 'Asus'), ('HP', 'HP'), ('Lenovo', 'Lenovo'), ('Samsung', 'Samsung'), ('Xiaomi', 'Xiaomi')], max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('weight', models.FloatField()),
                ('display', models.DecimalField(decimal_places=1, max_digits=3)),
                ('ram', models.IntegerField()),
                ('processor', models.CharField(choices=[('Intel', 'Intel'), ('AMD', 'AMD'), ('Apple', 'Apple'), ('Эльбрус', 'Эльбрус'), ('Байкал', 'Байкал')], max_length=10)),
            ],
        ),
    ]
