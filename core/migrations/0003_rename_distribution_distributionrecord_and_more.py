# Generated by Django 5.1.1 on 2024-10-15 17:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_remove_employee_password_alter_healthfacility_email_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Distribution",
            new_name="DistributionRecord",
        ),
        migrations.RenameModel(
            old_name="Storage",
            new_name="StorageRecord",
        ),
    ]