# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
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
class Member(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    show_name = models.CharField("Nom affiché", max_length=50, null=True)
    list_role = (
        ('C', 'Concurrent'),
        ('J', 'Jury'),
        ('A', 'Admin')
    )
    role = models.CharField("Rôle", max_length=1, choices=list_role, default='C')
    associated_key = models.CharField("Clé associée", max_length=50, null=True)

    def __unicode__(self):
        return self.user.username

class Challenge(models.Model):
    title = models.CharField("Titre", max_length=100)
    is_open = models.BooleanField("Ouvert", default=False)
    start_date = models.DateTimeField("Date de début", default=now)
    stop_date = models.DateTimeField("Date de fin", default=now)
    subs_start_date = models.DateTimeField("Date de début d'inscription", default=now)
    subs_stop_date = models.DateTimeField("Date de fin d'inscription", default=now)
    subm_start_date = models.DateTimeField("Date de début de soumission", default=now)
    subm_stop_date = models.DateTimeField("Date de fin de soumission", default=now)

    def __unicode__(self):
        return self.title

class AssociatedKey(models.Model):
    candidate = models.ForeignKey(Member)
    challenge = models.ForeignKey(Challenge)
    associated_key = models.CharField("Clé d'association", max_length=50)

    def __unicode__(self):
        return self.associated_key

class Movie(models.Model):
    challenge = models.ForeignKey(Challenge)
    associated_key = models.OneToOneField(AssociatedKey, unique=True)
    title = models.CharField("Titre", max_length=120,
                             help_text="Ce titre sera aussi utilisé sur "
                                       "notre compte DailyMotion")
    movie_url = models.URLField("Lien vers la vidéo", max_length=200, null=True)
    description = models.TextField("Description",
                                   help_text="Cette description sera aussi "
                                             "utilisée sur notre compte "
                                             "DailyMotion")
    submit_date = models.DateTimeField("Date de soumission",
                                       help_text="La date doit être insérée "
                                                 "sous forme jj/mm/aaaa "
                                                 "hh:mm:ss",
                                       default=now)
    published = models.BooleanField("Publié", default=False)

    def __unicode__(self):
        return self.title

"""
class Vote(models.Model):
    id_movie = models.ForeignKey(Movie)
    id_jury = models.ForeignKey(Members)
    artistic_note = notes
    scientific_note = notes
    pedagogic_note = notes
    vulgarisation_note = notes
    originality_note = notes
    jury_comment = models.TextField("Votre commentaire :")
"""
