from django.contrib import admin
from .models import Admin,Student,Question,Marks
# Register your models here.

admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Marks)
