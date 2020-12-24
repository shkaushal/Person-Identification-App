from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    # is_manager = models.BooleanField(default=False)

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

# class Manager(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

class Aadhar(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    aadhar_no = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "Aadhar"

class Address(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=6)
    class Meta:
        verbose_name_plural = "Address"

class Qualification(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    institute_name = models.CharField(max_length=50)
    yop = models.CharField(max_length=4)
    percent = models.CharField(max_length=3)

class Bank(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    account_no = models.CharField(max_length = 10)
    bank_name = models.CharField(max_length = 50)
    ifsc_code = models.CharField(max_length = 10)

class Details(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    full_name = models.CharField(max_length=50)
    dob = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    class Meta:
        verbose_name_plural = "Details"
    
class JobExperience(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    company_name = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    yoe = models.CharField(max_length=4)
    class Meta:
        verbose_name_plural = "JobExperience"



