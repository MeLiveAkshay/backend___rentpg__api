from django.contrib import admin
from .models import UserDetails,BookingDetails
# Register your models here.
@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_email', 'user_phone', 'profession')
    search_fields = ('user_name', 'user_email', 'user_phone')
    list_filter = ('profession',)


@admin.register(BookingDetails)
class BookingDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'booking_id', 'customer_name', 'customer_email','room_id','user_id',
        'check_in', 'check_out', 'is_confirmed', 'user', 'room'
    )
    search_fields = ('customer_name', 'customer_email', 'customer_phone')
    list_filter = ('is_confirmed', 'check_in', 'check_out')
