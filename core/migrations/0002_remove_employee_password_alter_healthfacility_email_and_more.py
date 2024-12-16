# Generated by Django 5.1.1 on 2024-10-14 14:02

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="password",
        ),
        migrations.AlterField(
            model_name="healthfacility",
            name="email",
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="healthfacility",
            name="name",
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name="healthfacility",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, null=True, region=None, unique=True
            ),
        ),
    ]