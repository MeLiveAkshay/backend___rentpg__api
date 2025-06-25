from django.db import models
from django.utils import timezone

from owner.models import Room

# Create your models here.
class UserDetails(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    user_phone = models.CharField(max_length=15)
    profession = models.CharField(max_length=100)
    address = models.TextField()
    current_address = models.TextField()

    def __str__(self):
        return self.user_name



class ContactDetails(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class RoomBooked(models.Model):
    booking_id = models.CharField(max_length=20, unique=True)

    # Room info
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    pg_name = models.CharField(max_length=255)
    pg_owner = models.CharField(max_length=255)
    room_type = models.CharField(max_length=100)
    room_price = models.DecimalField(max_digits=10, decimal_places=2)

    # User info
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    # System fields
    booking_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.booking_id} - {self.name}"
