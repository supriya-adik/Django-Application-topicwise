from django.db import models

# Create your models here.
class Student(models.Model) :
    sr=models.IntegerField()
    name=models.CharField(max_length=30)
    marks=models.IntegerField()

    def __str__(self):
        return  self.name