from django import forms
from django.core import validators
from .models import Home_Detail

class UserRagistrations(forms.ModelForm):
    class Meta:
        model = Home_Detail
        fields =  ['name', 'email','phone']
        labels = {'name':'Enter Name', 'email':'Enter Email'}
        widgets = {
            'name':forms.TextInput({'placeholder':'yaha name likho'})
        }