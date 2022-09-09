from django.urls import path
from .views import service_view

urlpatterns =[
    path('services/',service_view,name="services")
]