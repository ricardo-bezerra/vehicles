from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from car.api import viewsets as carviewsets


from customer.api import viewsets as customerviewsets

from employee.api import viewsets as employeeviewsets

from django.conf.urls.static import static

from django.conf import settings


route = routers.DefaultRouter()


route.register(r'car', carviewsets.CarViewset, basename='Car')

route.register(r'customer', customerviewsets.CustomerViewset, basename='Customer')

route.register(r'employee', employeeviewsets.EmployeeViewset, basename='Employee')


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('vehicles/', include(route.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
