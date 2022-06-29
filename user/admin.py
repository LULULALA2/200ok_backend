from django.contrib import admin

from user.models import User
from user.models import UserInfo

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'fullname',)
    list_display_links = ('username', )
    list_filter = ('username', )
    search_fields = ('username',)

    fieldsets = (
        ("info", {'fields': ('username', 'password', 'fullname', 'join_date',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active', )}),)

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date', )
        else:
            return ('join_date', )


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(UserInfo)


