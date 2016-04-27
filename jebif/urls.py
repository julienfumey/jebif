# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from bioinfuse import views as bviews
from django.conf import settings
from django.conf.urls.static import static

ROOT = settings.ROOT_URL

urlpatterns = [
    # Administration
    url(r'^%sadmin/' % ROOT, include(admin.site.urls)),
    # Home
    url(r'^%s$' % ROOT, bviews.index, name='index'),
    # Member
    url(r'^%saccounts/login/$' % ROOT, 'django.contrib.auth.views.login'),
    url(r'^%saccounts/logout/$' % ROOT, 'django.contrib.auth.views.logout', {'next_page': '/%s' % ROOT}),
    url(r'^%ssubscribe/$' % ROOT, bviews.subscribe, name='subscribe'),
    url(r'^%sedit_profile/(?P<member>[0-9]+)' % ROOT, bviews.edit_profile, name='edit_profile'),
    url(r'^%smanage_members' % ROOT, bviews.list_members, name="manage_members"),
    url(r'^%sedit_member/(?P<member>[0-9]+)' % ROOT, bviews.edit_member, name="edit_member"),
    url(r'^%ssubmit_movie/(?P<member>[0-9]+)$' % ROOT, bviews.submit_movie, name="submit_movie"),
]
