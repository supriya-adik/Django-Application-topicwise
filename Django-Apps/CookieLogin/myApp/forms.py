from django import forms

class MyForm(forms.Form):
    name = forms.CharField(label='Your name',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Name'}))
    email = forms.EmailField(label='Your email',
                            max_length=100,
                            widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter Email'}))