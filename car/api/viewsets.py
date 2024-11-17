from rest_framework import viewsets
from car.api import serializers
from car import models

class CarViewset(viewsets.ModelViewSet):

    serializer_class = serializers.CarSerializer
    queryset = models.Car.objects.all()
