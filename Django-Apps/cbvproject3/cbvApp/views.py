from django.shortcuts import render
from .models import company
from  django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class companyListview(ListView) :
    model=company
    #default template_name:company_list.html
    #default context_object_name:company_li st
class companyDetailView(DetailView) :
    model=company
    #default template_name:company_detail.html
    #default context_object_name:company or object
class companyCreateView(CreateView):
    model=company
    fields = ['name', 'location','ceo']     

class companyUpdateView(UpdateView) :
    model=company
    fields=['name','location','ceo']

class companyDeleteView(DeleteView) :
    model=company
    success_url=reverse_lazy('companyListview')