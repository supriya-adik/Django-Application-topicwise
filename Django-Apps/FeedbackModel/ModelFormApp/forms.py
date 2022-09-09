from django import forms
from ModelFormApp.models import student

class studentForm(forms.ModelForm) :
    class Meta :
        model=student
        fields=('name','marks')
