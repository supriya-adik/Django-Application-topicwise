from django import forms
from django.core import validators

def starts_with_d(value) :
    if value[0].lower()!='d' :
        raise forms.ValidationError('Name Should be startswith d|D')
    
class FeedBackForm(forms.Form) :
    name=forms.CharField()
    rollno=forms.IntegerField()
    email = forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)

    # def clean_name(self) :
    #     inputname=self.cleaned_data['name']
    #     print("Validating Rollno.")
    #     if len(inputname)<4 :
    #         raise forms.ValidationError('The length shound be greater than 4')
    #     return inputname
        
    def clean(self) :
        print("Total Form validation ..")
        total_clean =super().clean()
        inputname=total_clean['name']
        rollno=total_clean['rollno']
        if inputname[0].lower()!='d':
            raise forms.ValidationError('Name should be starts with D|d')
        if rollno <=0 :
           raise forms.ValidationError("Roll No should be greater than 0")