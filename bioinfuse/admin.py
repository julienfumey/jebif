from django.contrib import admin
from bioinfuse.models import *

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_filter = ('user', 'show_name', 'role')
    list_display = ('user', 'show_name', 'role')

admin.site.register(Member, MemberAdmin)
