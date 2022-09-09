from django import forms

class AddItem(forms.Form) :
    name=forms.CharField()
    qty=forms.IntegerField()