from django import forms
from main.models import User, Season, Matchday, Round
from django.core import validators

        
class UserFormSignUp(forms.ModelForm):
    class Meta:
        model = User
        fields = ('login', 'email', 'password')
        widgets={
            'password': forms.PasswordInput()
        }


class UserFormSignIn(forms.ModelForm):
    class Meta:
        model = User
        fields = ('login', 'password')

