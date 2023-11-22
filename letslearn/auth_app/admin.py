from django.contrib import admin
from .models import Login,Teacher,Student
# Register your models here.
admin.site.register(Login)
admin.site.register(Student)
admin.site.register(Teacher)