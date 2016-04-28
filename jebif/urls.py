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
    # Member
    url(r'^%slogin/$' % ROOT, auth_views.login, name="login"),
    url(r'^%saccounts/logout/$' % ROOT, auth_views.logout, {'next_page': '/%s'%BROOT}, name="logout"),
    url(r'%sbioinfuse/' % ROOT, include('bioinfuse.urls')),
]
