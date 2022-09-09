from django.urls import path
from testApp import views
urlpatterns = [
    path('firstwish/', views.tempview),
]
