from django import forms
from django.forms.models import ModelForm
from main.models import User, Season, Round, Matchday

        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['login', 'email', 'password']


class SeasonForm(ModelForm):
    class Meta:
        model = Season


class RoundForm(ModelForm):
    class Meta:
        model = Round


class MatchdayForm(ModelForm):
    class Meta:
        model = Matchday

