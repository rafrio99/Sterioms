# Generated by Django 5.1.1 on 2024-10-21 03:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_batch_barcode_department_barcode_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="LoginCode",
            fields=[
                (
                    "id",
                    models.CharField(
                        editable=False,
                        max_length=15,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("code", models.CharField(max_length=10)),
                ("added", models.TimeField(auto_now=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.employee"
                    ),
                ),
            ],
        ),
    ]
