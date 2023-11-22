from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    user_type = models.CharField(max_length=10, choices=[('teacher', 'Teacher'), ('student', 'Student')], default='student')

class Teacher(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    login_id = models.ForeignKey(
        Login,
        on_delete = models.CASCADE
    )    
    email = models.EmailField(max_length=254)
    phone_no = models.CharField(max_length=10)

class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    login_id = models.ForeignKey(
        Login,
        on_delete = models.CASCADE
    )    
    email = models.EmailField(max_length=254)
    phone_no = models.CharField(max_length=10)

