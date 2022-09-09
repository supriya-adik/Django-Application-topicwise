from django.contrib import admin
from .models import NameModel,AgeModel,GfModel
# Register your models here.
admin.site.register(NameModel)
admin.site.register(AgeModel)
admin.site.register(GfModel)