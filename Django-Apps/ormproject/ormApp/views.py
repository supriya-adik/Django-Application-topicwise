from django.shortcuts import render
from .models import Employee,CustomManager,proxyEmp
from django.db.models import Q
from django.db.models import Avg,Sum,Max,Min,Count
# Create your views here.
from django.db.models.functions import Lower

def show_emp(request) :
    employee=proxyEmp.objects.all()
    return render(request,'emp.html',{'emp':employee})






def display_view(request) :
    avg=Employee.objects.all().aggregate(Avg('esal'))
    sum=Employee.objects.all().aggregate(Sum('esal'))
    min=Employee.objects.all().aggregate(Min('esal'))
    max = Employee.objects.all().aggregate(Max('esal'))
    count=Employee.objects.all().aggregate(Count('esal'))


    dict={'avg':avg,'sum':sum,'min':min,'max':max,'count':count}
    return render(request,'aggregate.html',dict)
