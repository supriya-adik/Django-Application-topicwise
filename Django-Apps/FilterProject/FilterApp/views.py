from django.shortcuts import render
from FilterApp.models import FilterModel
# Create your views here.
def Upper_view(request) :
    data=FilterModel.objects.all()
    return render(request,'FilterApp/index.html',{'data':data})
