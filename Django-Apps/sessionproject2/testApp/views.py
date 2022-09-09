from django.shortcuts import render
from testApp.forms import AddItem
# Create your views here.
def add_item(request) :
    form=AddItem()
    if request.method=='POST' :
        form=AddItem(request.POST)
        name=request.POST['name']
        qty=request.POST['qty']
        request.session[name]=qty
        request.session.set_expiry(120)
    return render(request,'index.html',{'form':form})

def display_view(request) :
    del request.session['tomato']
    return render(request,'display.html')

def session_view(request) :
    session=request.session
    age=session.get_expiry_age()
    date=session.get_expiry_date()
    print("Age:",age,"\nDate:",date)
    return render(request,'index.html')

