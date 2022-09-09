from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from .models import Book
# Create your views here.

def info_view(request) :
    books=Book.objects.all()
    return render(request,'cbvApp/results.html',{'books':books})

class BookListView(ListView):
    model=Book
    template_name ='cbvApp/book_list.html'
    context_object_name = 'list_of_books'
    #default template:book_list.html
    #default context object:book_list

class BookDetailView(DetailView) :
    model=Book
    template_name = 'cbvApp/book_detail.html'

    #default template :book_detail.html
    #default context object :book


def hello(request) :
    return HttpResponse('<h2>Hii Welcome....!!!</h2>')

class HelowordView(View) :
    def get(self,request) :
        return  HttpResponse('<h1> This is from class based view....!</h1>')

class HelowordTemplate(TemplateView) :
    template_name = 'cbvApp/results.html'

class HelowordTemplateContext(TemplateView) :
    template_name = 'cbvApp/emp.html'
    def get_context_data(self, **kwargs):
      context=super().get_context_data(**kwargs)
      context['name'] ="Durga"
      context['subject']="Python"
      context['marks'] =100
      return context

