from django.shortcuts import render

# Create your views here.
def count_view(request) :
    newcount=int(request.COOKIES.get('count',0))+1
    
    response=render(request,'index.html',{'count':newcount})
    response.set_cookie('count',newcount,max_age=20)
    return response
        