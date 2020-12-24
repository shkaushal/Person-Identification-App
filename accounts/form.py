from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Staff,Aadhar,Address,Qualification,Bank,Details,JobExperience

class StaffSignUpForm(UserCreationForm):
    full_name = forms.CharField(required=True)
    aadhar_no = forms.IntegerField(required=True)
    is_active = forms.BooleanField(required=True)
    street = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    postal_code = forms.IntegerField(required=True)
    institute_name = forms.CharField(required=True)
    yop = forms.IntegerField(required=True)
    percent = forms.IntegerField(required=True)
    account_no = forms.IntegerField(required=True)
    bank_name = forms.CharField(required=True)  
    ifsc_code = forms.CharField(required=True)
    full_name = forms.CharField(required=True)
    dob = forms.DateField(required=True)
    blood_group = forms.CharField(required=True)
    contact_no = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    company_name = forms.CharField(required=True)
    role = forms.CharField(required=True)
    yoe = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_staff = True
        user.save()
        staff = Staff.objects.create(user=user)
        # staff.phone_number=self.cleaned_data.get('phone_number')
        # staff.location=self.cleaned_data.get('location')
        staff.save()
        aadhar = Aadhar.objects.create(user=user)
        aadhar.aadhar_no = self.cleaned_data.get('aadhar_no')
        aadhar.is_active = self.cleaned_data.get('is_active')
        aadhar.save()
        address = Address.objects.create(user=user)
        address.street = self.cleaned_data.get('street')
        address.city = self.cleaned_data.get('city')
        address.state = self.cleaned_data.get('state')
        address.postal_code = self.cleaned_data.get('postal_code')
        address.save()
        qualification = Qualification.objects.create(user=user)
        qualification.institute_name = self.cleaned_data.get('institute_name')
        qualification.yop = self.cleaned_data.get('yop')
        qualification.percent = self.cleaned_data.get('percent')
        qualification.save()
        bank = Bank.objects.create(user=user)
        bank.account_no = self.cleaned_data.get('account_no')
        bank.bank_name = self.cleaned_data.get('bank_name')
        bank.ifsc_code = self.cleaned_data.get('ifsc_code')
        bank.save()
        details = Details.objects.create(user=user)
        details.full_name = self.cleaned_data.get('full_name')
        details.dob = self.cleaned_data.get('dob')
        details.blood_group = self.cleaned_data.get('blood_group')
        details.contact_no = self.cleaned_data.get('contact_no')
        details.email = self.cleaned_data.get('email')
        details.save()
        jobExperience = JobExperience.objects.create(user=user)
        jobExperience.company_name = self.cleaned_data.get('company_name')
        jobExperience.role = self.cleaned_data.get('role')
        jobExperience.yoe = self.cleaned_data.get('yoe')
        jobExperience.save()
        return user

# class ManagerSignUpForm(UserCreationForm):
#     name = forms.CharField(required=True)
    

#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_manager = True
#         user.is_staff = True
#         user.full_name = self.cleaned_data.get('full_name')
#         user.save()
#         manager = Manager.objects.create(user=user)
#         # manager.phone_number=self.cleaned_data.get('phone_number')
#         # manager.designation=self.cleaned_data.get('designation')
#         manager.save()
#         return user
