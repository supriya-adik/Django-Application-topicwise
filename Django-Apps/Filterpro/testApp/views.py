from django.shortcuts import render
from .models import Student
# Create your views here.
def filterview(request) :
    data =Student.objects.all()
    return render(request,'truncate.html',{'data':data})