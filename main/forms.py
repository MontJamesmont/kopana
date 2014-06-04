from django import forms
from django.forms.models import ModelForm
from main.models import User, Season, Matchday, Round
from django.core import validators

        
class UserFormSignUp(forms.ModelForm):
    class Meta:
        model = User
        fields = ('login', 'email', 'password')
        widgets={
            'password': forms.PasswordInput()
        }


class SeasonForm(ModelForm):
    class Meta:
        model = Season


class RoundForm(ModelForm):
    class Meta:
        model = Round


class MatchdayForm(ModelForm):
    class Meta:
        model = Matchday

class UserFormSignIn(ModelForm):
	class Meta:
		model = User
		fields = ('login', 'password')
        
class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        
class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
