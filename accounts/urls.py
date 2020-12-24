from django.urls import path
from .import  views

urlpatterns=[
     # path('register/',views.register, name='register'),
     path('register/',views.staff_register.as_view(), name='register'),
     # path('manager_register/',views.manager_register.as_view(), name='manager_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]