from django.shortcuts import render

# Create your views here.
def service_view(request) :
    context = {'services': 'active'}
    return render(request,'serv/service.html',context=context)