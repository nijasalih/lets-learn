app_name="auth_app"

from django.urls import path
from .views import index,reg_stud,reg_teach,login
urlpatterns = [
    path('',index),
    path('register/student/',reg_stud,name="register_student"),
    path('register/teacher/',reg_teach,name="register_teacher"),
    path('login/',login,name="login")
]
