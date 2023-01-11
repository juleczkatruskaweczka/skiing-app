from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Polyski_app.models import user, event, Tracks
from django.contrib.auth.models import Group
from django.contrib import admin

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email','username','is_admin','is_staff','is_free')
    search_fields = ('email','username')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(user, AccountAdmin)
admin.site.register(event)
admin.site.unregister(Group)
admin.site.register(Tracks)