from django.contrib import admin
from .models import StudentInfo,TeacherInfo,StudentInfo1,TeacherInfo1,ContactInfo1,Parent1,Parent2,Child
# Register your models here.
admin.site.register(StudentInfo)
admin.site.register(TeacherInfo)
#multipletable
admin.site.register(StudentInfo1)
admin.site.register(TeacherInfo1)
admin.site.register(ContactInfo1)
#multilevel
admin.site.register(Parent1)
admin.site.register(Parent2)
admin.site.register(Child)

