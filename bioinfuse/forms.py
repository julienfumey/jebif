# -*- coding: utf-8 -*-
from django import forms
from .models import *
from django.contrib.auth.models import User

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


class LoginUserForm(forms.ModelForm):
    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)

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
'''

class SubmitMovieForm(forms.ModelForm):
    file_movie = forms.FileField(label="Votre vidéo")
    class Meta:
        model = Movie
        exclude = ('challenge', 'associated_key', 'movie_url', 'published')
