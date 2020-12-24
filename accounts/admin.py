from django.contrib import admin
from .models import User, Staff, Aadhar, Address, Qualification, Bank, Details, JobExperience

admin.site.register(User)
admin.site.register(Staff)
# admin.site.register(Manager)
admin.site.register(Aadhar)
admin.site.register(Address)
admin.site.register(Qualification)
admin.site.register(Bank)
admin.site.register(Details)
admin.site.register(JobExperience)