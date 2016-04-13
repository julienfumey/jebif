from django.contrib import admin
from bioinfuse.models import *

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'show_name', 'role')# 'user.first_name', 'user.last_name', 'user.email')


admin.site.register(Member, MemberAdmin)
