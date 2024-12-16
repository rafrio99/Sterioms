# Generated by Django 5.1.1 on 2024-10-21 09:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0009_logincode"),
    ]

    operations = [
        migrations.CreateModel(
            name="LoginTable",
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
                ("token", models.CharField(max_length=30)),
                ("last_login", models.DateTimeField(auto_now_add=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.employee"
                    ),
                ),
            ],
        ),
    ]