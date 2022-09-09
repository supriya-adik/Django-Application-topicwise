from django.shortcuts import render
from testApp.forms import NameForm,AgeForm,GfForm
# Create your views here.
def name_view(request) :
    form=NameForm()
    return render(request,'name.html',{'form':form})

def age_view(request) :
    name=request.GET['names']
    request.session['Myname'] =name
    form=AgeForm()
    return render(request,'age.html',{'form':form})

def gf_view(request) :
    age=request.GET['age']
    request.session['Myage'] =age
    form=GfForm()
    return render(request,'gf.html',{'form':form})

def result_view(request) :
    gf=request.GET['gfs']
    request.session['Mygf'] =gf
    return render(request,'result.html')