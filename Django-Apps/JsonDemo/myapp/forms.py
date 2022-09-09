from dataclasses import field
from socket import fromshare
from django import fromshare
from .models import Product
class ProductForm(forms.ModelForm) :
    class Meta :
        model = Product
        fields = "__all__"
    
    def clean_price(self) :
        price = self.