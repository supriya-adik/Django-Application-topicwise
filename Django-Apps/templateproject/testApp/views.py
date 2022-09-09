from django.shortcuts import render
import datetime
# Create your views here.
def tempview(request) :
    d=datetime.datetime.now();
    dict={'date_msg':d}
    return render(request,'testApp/wish.html',context=dict)
