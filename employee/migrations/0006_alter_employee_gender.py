# Generated by Django 5.1.3 on 2024-11-17 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_employee_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(default='', max_length=1),
        ),
    ]
