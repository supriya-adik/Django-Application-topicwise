from django.db import models

# Create your models here.
#custom_manger
class CustomManager(models.Manager) :
    def get_queryset(self):
        return super().get_queryset().filter(ename__istartswith='J')

    def get_emp_sal_range(self,esal1,esal2):
        return  super().get_queryset().filter(esal__range=(esal1,esal2))
    def get_emp_sorted_by(self,param):
        return super().get_queryset().order_by(param)


class CustomManger2(models.Manager) :
   def get_queryset(self):
       return  super().get_queryset().filter(eno__exact=1)

class Employee(models.Model) :
    eno =models.IntegerField()
    ename=models.CharField(max_length=40)
    esal = models.CharField(max_length=40)
    eaddr = models.CharField(max_length=40)
    objects=CustomManager()

class proxyEmp(Employee) :
    objects = CustomManger2()
    class Meta:
        proxy=True

