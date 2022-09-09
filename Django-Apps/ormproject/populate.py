import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ormproject.settings')

import django
django.setup()

from ormApp.models import Employee
from faker import Faker
from random import *
faker=Faker()
def populate(n) :
    for i in range(n) :
        feno=randint(1,1000)
        fename=faker.name()
        fesal=randint(10000,25000)
        faddr=faker.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=faddr)
populate(20)

