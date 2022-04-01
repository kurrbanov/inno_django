# Generated by Django 4.0.3 on 2022-03-31 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_cart_laptop'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaptopPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.FilePathField()),
                ('laptop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='application.laptop')),
            ],
        ),
    ]