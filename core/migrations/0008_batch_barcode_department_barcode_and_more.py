# Generated by Django 5.1.1 on 2024-10-19 14:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_equipment_barcode"),
    ]

    operations = [
        migrations.AddField(
            model_name="batch",
            name="barcode",
            field=models.ImageField(blank=True, null=True, upload_to="barcodes/batch/"),
        ),
        migrations.AddField(
            model_name="department",
            name="barcode",
            field=models.ImageField(
                blank=True, null=True, upload_to="barcodes/department/"
            ),
        ),
        migrations.AddField(
            model_name="distributionrecord",
            name="barcode",
            field=models.ImageField(
                blank=True, null=True, upload_to="barcodes/distro/"
            ),
        ),
        migrations.AddField(
            model_name="employee",
            name="barcode",
            field=models.ImageField(
                blank=True, null=True, upload_to="barcodes/employees/"
            ),
        ),
        migrations.AddField(
            model_name="healthfacility",
            name="barcode",
            field=models.ImageField(
                blank=True, null=True, upload_to="barcodes/facility/"
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="barcode",
            field=models.ImageField(
                blank=True, null=True, upload_to="barcodes/package/"
            ),
        ),
        migrations.AddField(
            model_name="stage",
            name="barcode",
            field=models.ImageField(blank=True, null=True, upload_to="barcodes/stage/"),
        ),
        migrations.AddField(
            model_name="sterilizationmethod",
            name="barcode",
            field=models.ImageField(
                blank=True, null=True, upload_to="barcodes/sterilization/"
            ),
        ),
        migrations.AddField(
            model_name="storagerecord",
            name="barcode",
            field=models.ImageField(blank=True, null=True, upload_to="barcodes/store/"),
        ),
        migrations.AlterField(
            model_name="employeestatus",
            name="id",
            field=models.CharField(
                editable=False, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="barcode",
            field=models.ImageField(
                blank=True, null=True, upload_to="barcodes/equipment/"
            ),
        ),
        migrations.AlterField(
            model_name="role",
            name="id",
            field=models.CharField(
                editable=False, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
