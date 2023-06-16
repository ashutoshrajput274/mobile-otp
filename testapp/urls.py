from django.contrib import admin
from django.urls import path
from testapp.views import *

urlpatterns = [
    path('send_otp/', send_otp),
    path('verify_otp/',verify_otp),
    
]