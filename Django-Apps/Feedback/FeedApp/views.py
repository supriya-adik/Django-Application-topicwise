from django.shortcuts import render
from . import forms
# Create your views here.
def FeedbackView(request) :
    form=forms.FeedBackForm()
    if request.method=='POST' :
        form=forms.FeedBackForm(request.POST)
        if form.is_valid() :
            print("Form valid ...")
            print("RollNo:",form.cleaned_data['rollno'])
            print("Name:",form.cleaned_data['name'])
            print("Email:",form.cleaned_data['email'])
            print("Feedback:",form.cleaned_data['feedback'])
    return render(request,'feedback.html',{'form':form})