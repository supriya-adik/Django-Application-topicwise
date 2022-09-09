from django.db import models

# Create your models here.
class ContactInfo(models.Model) :
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=60)
    email=models.CharField(max_length=15)
    class Meta :
        abstract=True

class StudentInfo(ContactInfo) :
    rollno=models.IntegerField()
    marks=models.IntegerField()

class TeacherInfo(ContactInfo) :
    subject=models.CharField(max_length=30)
    salary=models.IntegerField()

#multi table inheritance
class ContactInfo1(models.Model) :
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=60)
    email=models.CharField(max_length=15)

class StudentInfo1(ContactInfo) :
    rollno=models.IntegerField()
    marks=models.IntegerField()

class TeacherInfo1(ContactInfo) :
    subject=models.CharField(max_length=30)
    salary=models.IntegerField()

#multiple inheritance

class Parent1(models.Model) :
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=60)
    email=models.CharField(max_length=15)

class Parent2(Parent1) :
    rollno=models.IntegerField()
    marks=models.IntegerField()

class Child(Parent2) :
    subject=models.CharField(max_length=30)
    salary=models.IntegerField()
