# Generated by Django 5.1.3 on 2024-11-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='sale_date',
            field=models.DateField(),
        ),
    ]
