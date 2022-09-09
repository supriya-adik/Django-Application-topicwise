from .models import NameModel,GfModel,AgeModel
from django import forms

class NameForm(forms.ModelForm) :
   class Meta :
        model =NameModel
        fields ='__all__'

class AgeForm(forms.ModelForm):
  class Meta :
    model=AgeModel
    fields ='__all__'

class GfForm(forms.ModelForm) :
   class Meta:
    model =GfModel
    fields ='__all__'