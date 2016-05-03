# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from bioinfuse import views as bviews

ROOT = settings.ROOT_URL

BROOT = "%sbioinfuse/" % ROOT

urlpatterns = [
    # Administration
    url(r'^%sadmin/' % ROOT, include(admin.site.urls)),
    # Member login & logout
    url(r'^%slogin/$' % ROOT, auth_views.login, name="login"),
    url(r'^%saccounts/logout/$' % ROOT, auth_views.logout, {'next_page': '/%s'%BROOT}, name="logout"),
    # Home
    url(r'^%s$' % ROOT, bviews.home, name="home"),
    # BioInfuse
    url(r'%s' % BROOT, include('bioinfuse.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
