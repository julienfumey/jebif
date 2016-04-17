from django import forms
from models import *
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

class NewUserForm(forms.ModelForm):
    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'password', 'email',)

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('show_name',)

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('show_name',)

class ManageUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ManageMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('show_name', 'role')

'''
class NewChallenge(forms.ModelForm):
    class Meta:
        model = Challenge
        exclude = ()

class SubmitMovie(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ()
'''
