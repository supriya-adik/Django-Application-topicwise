from django.shortcuts import render
from ModelFormApp.models import student
from ModelFormApp.forms import studentForm
# Create your views here.
def studentview(request) :
    form=studentForm()
    if request.method=='POST' :
      form=studentForm(request.POST)
      if form.is_valid() :
          form.save()
    return render(request,'index.html',{'form':form})