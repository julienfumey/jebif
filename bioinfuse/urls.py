# -*- coding: utf-8 -*-
from django.conf.urls import url
from bioinfuse import views
from django.conf import settings

app_name = 'bioinfuse'

urlpatterns = [
    # Home
    url(r'^$', views.index, name='index'),
    # Member
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    url(r'^edit_profile/(?P<member>[0-9]+)', views.edit_profile, name='edit_profile'),
    url(r'^manage_members', views.list_members, name="manage_members"),
    url(r'^edit_member/(?P<member>[0-9]+)', views.edit_member, name="edit_member"),
    url(r'^submit_movie/(?P<member>[0-9]+)$', views.submit_movie, name="submit_movie"),
]
