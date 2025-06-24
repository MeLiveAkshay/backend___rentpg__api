from django.contrib import admin
from .models import UserDetails
# Register your models here.
@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_email', 'user_phone', 'profession')
    search_fields = ('user_name', 'user_email', 'user_phone')
    list_filter = ('profession',)

