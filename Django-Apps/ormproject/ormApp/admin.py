from django.contrib import admin
from.models import Employee,proxyEmp
# Register your models here.
class EmpAdmin(admin.ModelAdmin) :
    list_display=['eno','ename','esal','eaddr']

class ProxyAdmin(admin.ModelAdmin) :
   list_display = ['eno','ename']

admin.site.register(proxyEmp,ProxyAdmin)
admin.site.register(Employee,EmpAdmin)