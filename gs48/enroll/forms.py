from django.core import validators
from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ['name', 'password', 'email']
        labels = {'name': 'Enter Name', 'email': 'Enter Email',
                  'password': 'Enter Password'}
        error_messages = {
            'name': {'required': 'Name Field is empty'},
            'password': {'required': 'password Field is empty'}
        }
        widgets = {
            'password': forms.PasswordInput,
            'name': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Plz Enter Your Name'})
        }
