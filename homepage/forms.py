from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User  
from .models import Business
class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'email','phone']