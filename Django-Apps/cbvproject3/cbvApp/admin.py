from django.contrib import admin
from .models import company
# Register your models here.
class companyAdmin(admin.ModelAdmin) :
    list_display=['name','location','ceo']

admin.site.register(company,companyAdmin)