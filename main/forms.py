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
    confirmpassword = forms.CharField(label='Potwierdz haslo', widget=forms.PasswordInput())


class UserFormSignIn(forms.ModelForm):
    class Meta:
        model = User
        fields = ('login', 'email', 'password')