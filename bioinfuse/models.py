# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractBaseUser
from django.utils.dateformat import DateFormat
from django.utils.timezone import now

notes = (
			('0', '0'),
			('1', '1'),
			('2', '2'),
			('3', '3'),
			('4', '4'),
			('5', '5')
		)

# Create your models here.
#class Member(AbstractBaseUser):
class Member(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
#	username = models.CharField("Nom d'utilisateur", max_length=30)
#	first_name = models.CharField("Prénom", max_length=30)
#	last_name = models.CharField("Nom", max_length=30)
#	email = models.EmailField("Courriel", max_length=200)
#	password = models.CharField(max_length=32)
#	joined_date = models.DateTimeField()
    show_name = models.CharField("Nom affiché", max_length=50)
    list_role = (
                    ('C', 'Concurrent'),
                    ('J', 'Jury'),
                    ('A', 'Admin')
                )
    role = models.CharField("Rôle", max_length=1, choices=list_role, default='C')
    associated_key = models.CharField("Clé", max_length=50)
	
	#def __unicode__(self):
	#    return self.user.username

class Challenge(models.Model):
	title = models.CharField(max_length=100)
	is_open = models.BooleanField(default=False)
	start_date = models.DateTimeField() 
	stop_date = models.DateTimeField()

class AssociatedKey(models.Model):
	candidate = models.ForeignKey(Member)
	associated_key = models.CharField(max_length=50)

class Movie(models.Model):
	title = models.CharField(max_length=120)
	movie_url = models.URLField(max_length=200)
	associated_key = models.ForeignKey(AssociatedKey)
	description = models.TextField()
	submit_date = models.DateTimeField()
	published = models.BooleanField(default=False)

"""
class Vote(models.Model):
	id_movie = models.ForeignKey(Movie)
	id_jury = models.ForeignKey(Members)
	artistic_note = notes
	scientific_note = notes
	pedagogic_note = notes
	vulgarisation_note = notes
	originality_note = notes
	jury_comment = models.TextField()
"""
