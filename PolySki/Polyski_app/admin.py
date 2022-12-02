from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Polyski_app.models import user
from django.contrib.auth.models import Group
from django.contrib import admin

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email','username','is_admin','is_staff')
    search_fields = ('email','username')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(user, AccountAdmin)
admin.site.unregister(Group)