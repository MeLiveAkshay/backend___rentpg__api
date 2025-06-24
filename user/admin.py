from django.contrib import admin
from .models import UserDetails, ContactDetails

# Admin Branding
admin.site.site_header = 'RentPG Dashboard'
admin.site.site_title = 'RentPG Admin'
admin.site.index_title = 'Welcome to RentPG Administration'

# UserDetails Admin
@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_email', 'user_phone', 'profession')
    search_fields = ('user_name', 'user_email', 'user_phone')
    list_filter = ('profession',)


# ContactDetails Admin
@admin.register(ContactDetails)
class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at',)  # more meaningful filter
