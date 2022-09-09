from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('',views.hello,name="hello"),
    path('clsview/',views.HelowordView.as_view(),name="HelowordView"),
    path('contextview/',views.HelowordTemplateContext.as_view(), name="HelowordTemplateContext"),
    path('bookview/', views.BookListView.as_view(), name="BookListView"),
    path('<pk>/', views.BookDetailView.as_view(), name="BookDetailView")

]
