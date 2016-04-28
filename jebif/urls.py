# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from bioinfuse import views as bviews
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

ROOT = settings.ROOT_URL

BROOT = "%sbioinfuse/" % ROOT

urlpatterns = [
    # Administration
    url(r'^%sadmin/' % ROOT, include(admin.site.urls)),
    # Home
    url(r'^%s$' % BROOT, bviews.index, name='index'),
    # Member
    url(r'^%slogin/$' % ROOT, auth_views.login),
    url(r'^%saccounts/logout/$' % ROOT, auth_views.logout, {'next_page': '/%s'%BROOT}),
    url(r'^%ssubscribe/$' % BROOT, bviews.subscribe, name='subscribe'),
    url(r'^%sedit_profile/(?P<member>[0-9]+)' % BROOT, bviews.edit_profile, name='edit_profile'),
    url(r'^%smanage_members' % BROOT, bviews.list_members, name="manage_members"),
    url(r'^%sedit_member/(?P<member>[0-9]+)' % BROOT, bviews.edit_member, name="edit_member"),
    url(r'^%ssubmit_movie/(?P<member>[0-9]+)$' % BROOT, bviews.submit_movie, name="submit_movie"),
]
