# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

ROOT = settings.ROOT_URL

BROOT = "%sbioinfuse/" % ROOT

urlpatterns = [
    # Administration
    url(r'^%sadmin/' % ROOT, include(admin.site.urls)),
    # BioInfuse
    url(r'^%s' % BROOT, include('bioinfuse.urls')),
    # Member
    url(r'^%slogin/$' % ROOT, auth_views.login, name="login"),
    url(r'^%saccounts/logout/$' % ROOT, auth_views.logout, {'next_page': '/%s'%BROOT}, name="logout"),
    url(r'^%ssubscribe/' % BROOT, include('bioinfuse.urls', namespace='subscribe')),
    url(r'^%sedit_profile/(?P<member>[0-9]+)' % BROOT, include('bioinfuse.urls', namespace='edit_profile')),
    url(r'^%smanage_members' % BROOT, include('bioinfuse.urls', namespace="manage_members")),
    url(r'^%sedit_member/(?P<member>[0-9]+)' % BROOT, include('bioinfuse.urls', namespace="edit_member")),
    url(r'^%ssubmit_movie/(?P<member>[0-9]+)' % BROOT, include('bioinfuse.urls', namespace="submit_movie")),
]
