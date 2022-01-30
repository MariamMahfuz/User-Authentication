from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
class Student_info(models.Model):
    student_id=models.CharField(max_length=30,null=True,blank=True)
    student_name=models.CharField(max_length=50,blank=True)
    phone_number=models.CharField(max_length=15,blank=True)

    def __str__(self):
        return self.student_name