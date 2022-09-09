from django.shortcuts import render

# Create your views here.
def home(request) :
    return render(request,'base.html')

def movie(request) :
    return render(request,'movie.html')

def sports(request) :
    return render(request,'sports.html')