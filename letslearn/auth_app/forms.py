from django.forms import ModelForm
from .models import Login,Teacher,Student


class CreateLoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ('username','password')

class CreateTeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('first_name','last_name','email','phone_no')

class CreateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('first_name','last_name','email','phone_no')