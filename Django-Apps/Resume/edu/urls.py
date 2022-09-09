from django.urls import path
from .views import edu_view
urlpatterns =[
 path('skill/',edu_view,name='skill')
]
