# Generated by Django 4.0.3 on 2022-04-01 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_alter_laptopphoto_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptopphoto',
            name='laptop',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='application.laptop'),
        ),
    ]
