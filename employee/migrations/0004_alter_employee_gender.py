# Generated by Django 5.1.3 on 2024-11-16 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_gender_employee_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.BooleanField(blank=True, default='M'),
        ),
    ]
