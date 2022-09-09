from django.db import models

# Create your models here.
class NameModel(models.Model) :
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)

    def __str__(self):
        return  self.fname
class AgeModel(models.Model) :
  age=models.IntegerField()

  def __str__(self):
      return self.age

class GfModel(models.Model) :
    gf=models.CharField(max_length=10)

    def __str__(self):
        return self.gf