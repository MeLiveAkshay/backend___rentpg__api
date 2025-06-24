from django.contrib import admin
from .models import Owner,Room
# Register your models here.
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'pg_name', 'room_type', 'is_available', 'room_price', 'pg_owner')
    list_filter = ('room_type', 'is_available')
    search_fields = ('pg_name', 'room_location', 'pg_owner__name')