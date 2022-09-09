from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authApp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def display(request) :
    return render(request,'authApp/home.html')
@login_required
def javaexams(request) :
    return render(request,'authApp/java.html')

def pythonexams(request) :
    return render(request,'authApp/python.html')
    
def logout_view(request) :
    return render(request,'registration/logout.html')

def signup_view(request) :
    form=SignUpForm()
    if request.method=='POST' :
        form=SignUpForm(request.POST)
        User=form.save()
        User.set_password(User.password) 
        User.save()
        return HttpResponseRedirect('accounts/login')
    return render(request,'authapp/signup.html',{'form':form})