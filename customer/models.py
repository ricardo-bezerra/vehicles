from django.db import models
from uuid import uuid4

from datetime import date


class Customer(models.Model):
 
    id_customer = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    document = models.CharField(max_length=25)
    name = models.CharField(max_length=35, default=False, blank=True)
    gender = models.CharField(max_length=1, default="")
    occupation = models.CharField(max_length=55)
    birth = models.DateField()
    income = models.FloatField()
    service_date = models.DateField()
    sale_date = models.DateField()
    email = models.CharField(max_length=55, null=True)
    phone = models.CharField(max_length=20, null=True)
    create_at = models.DateField(auto_now_add=True)
