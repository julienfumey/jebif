from django.contrib import admin
from bioinfuse.models import *

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_filter = ('user', 'show_name', 'role')
    list_display = ('user', 'show_name', 'role')

class ChallengeAdmin(admin.ModelAdmin):
    list_filter = ('title', 'is_open', 'start_date', 'subs_start_date',
                   'subm_start_date')
    list_display = ('title', 'is_open', 'start_date', 'stop_date',
                    'subs_start_date', 'subs_stop_date', 'subm_start_date',
                    'subm_stop_date')

class AssociatedKeyAdmin(admin.ModelAdmin):
    list_filter = ('challenge', 'candidate')
    list_display = ('challenge', 'candidate')

admin.site.register(Member, MemberAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(AssociatedKey, AssociatedKeyAdmin)