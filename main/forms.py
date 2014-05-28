from django import forms
from main.models import User

        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['login', 'email', 'password']