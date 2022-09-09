from django import forms

class NameForm(forms.Form) :
    names=forms.CharField()

class AgeForm(forms.Form) :
    age=forms.IntegerField()

class GfForm(forms.Form) :
    gfs=forms.CharField()