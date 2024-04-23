from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Blog
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import permission_required

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ['Custom Fields', {'fields': ('profile_picture', 'bio', 'role')}],
    )
    
    
    def username_(self, obj):
        return obj.username 
    
    
    
    
    list_display = ['username', 'email', 'first_name', 'give_time', 'is_staff', 'date_joined']
    
    
    def give_time(self, obj):
        now = timezone.now()
        diffrence = now - obj.date_joined        
        days = diffrence.days
        hours = diffrence.seconds // 3600
        remainder_seconds = diffrence.seconds % 3600
        minutes = remainder_seconds // 60
        
        if hours >= 24:
            days += 1
            hours = 0  
        if days > 0:
            return f"{days} days, {hours} hours, {minutes} minutes ago"
        elif hours > 0:
            return f"{hours} hours, {minutes} minutes ago"
        else:
            return f"{minutes} minutes ago"

    give_time.short_description = 'Time since created'

        
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Blog)
