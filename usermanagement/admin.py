from django.contrib import admin
from .models import User_Management


# Register your models here.


class CustomeUserProfileAdmin(admin.ModelAdmin):
    list_display = ( 'id',
    'first_name', 'last_name', 'email', 'username', 'is_active', 'is_staff', 'is_superuser', 'created_on_display',
    'modified_on_display')

    def created_on_display(self, obj):
        return obj.created_on.strftime('%m/%d/%Y %H:%M') if obj.created_on else None

    created_on_display.short_description = 'Created On'

    def modified_on_display(self, obj):
        return obj.modified_on.strftime('%m/%d/%Y %H:%M') if obj.modified_on else None

    modified_on_display.short_description = 'Modified On'


admin.site.register(User_Management, CustomeUserProfileAdmin)
