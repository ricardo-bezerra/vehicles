# Generated by Django 5.1.3 on 2024-11-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='start_date',
            field=models.DateField(),
        ),
    ]