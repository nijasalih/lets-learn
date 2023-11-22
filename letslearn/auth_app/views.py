from django.shortcuts import render
from .forms import CreateLoginForm,CreateTeacherForm,CreateStudentForm
# Create your views here.
def index(request):
    return render(request,'auth_app/index.html')

def reg_teach(request):
    form1 = CreateTeacherForm 
    form2 = CreateLoginForm
    return render(request,'auth_app/register_teach.html',{'form1':form1,'form2':form2})

def reg_stud(request):
    form1 = CreateStudentForm
    form2 = CreateLoginForm
    return render(request,'auth_app/register_stud.html',{'form1':form1,'form2':form2})

def login(request):
    form = CreateLoginForm
    return render(request,'auth_app/login.html',{'form':form})
