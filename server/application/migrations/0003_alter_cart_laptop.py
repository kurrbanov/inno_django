# Generated by Django 4.0.3 on 2022-03-31 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='laptop',
            field=models.ManyToManyField(null=True, to='application.laptop'),
        ),
    ]
