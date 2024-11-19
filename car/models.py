from django.db import models
from uuid import uuid4


# def upload_image_car(instance, filename):
#    return f"{instance.id_car}, {filename}"


upload_image_car = lambda instance, filename: f"{instance.id_car}, {filename}"

# x = lambda a, b : a * b
# print(x(5, 6))

class Car(models.Model):
 
    id_car = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    brand = models.CharField(max_length=55)
    model = models.CharField(max_length=55)
    fuel = models.CharField(max_length=55)
    type = models.CharField(max_length=55) 
    release_year = models.DateField()
    state = models.CharField(max_length=15)
    color = models.CharField(max_length=25, null=True)
    quilometers = models.IntegerField()
    publishing_company = models.CharField(max_length=55)
    create_at = models.DateField(auto_now_add=True)

    image = models.ImageField(upload_to=upload_image_car, blank=True, null=True)
    