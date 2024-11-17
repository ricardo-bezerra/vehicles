from django.db import models
from uuid import uuid4


def upload_image_employee(instance, filename):
   return f"{instance.id_employee}, {filename}"


class Employee(models.Model):
 
    id_employee = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    serial_code = models.CharField(max_length=25)
    name = models.CharField(max_length=35, default=False, blank=True)
    gender = models.CharField(max_length=1, default="")
    business_unity = models.CharField(max_length=25)
    function = models.CharField(max_length=25)
    birth = models.DateField()
    start_date = models.DateField()
    create_at = models.DateField(auto_now_add=True)

    image = models.ImageField(upload_to=upload_image_employee, blank=True, null=True)
    