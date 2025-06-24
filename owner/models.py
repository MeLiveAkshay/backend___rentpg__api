from django.db import models

# Create your models here.


class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Room(models.Model):
    """
    Represents a rental PG room owned by an Owner.
    """
    room_id = models.AutoField(primary_key=True)
    total_room = models.IntegerField()
    pg_name = models.CharField(max_length=100)
    pg_owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="rooms")
    pg_image_url = models.URLField(blank=True, null=True)
    facility = models.TextField()
    amenity = models.TextField()
    room_type = models.CharField(max_length=50)
    is_available = models.CharField(
        max_length=3,
        choices=[('Yes', 'Yes'), ('No', 'No')],
        default='Yes'
    )
    room_location = models.CharField(max_length=200)
    room_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.pg_name} - {self.room_type} - {self.room_location}"

import random
import string
from django.db import models

def generate_booking_id():
    letters = ''.join(random.choices(string.ascii_uppercase, k=4))
    digits = ''.join(random.choices(string.digits, k=4))
    return letters + digits

class Booking(models.Model):
    BOOKING_STATUS_CHOICES = [
        ('rejected', 'Rejected'),
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
    ]

    booking_id = models.CharField(max_length=8, unique=True, primary_key=True, editable=False)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    booking_status = models.CharField(max_length=10, choices=BOOKING_STATUS_CHOICES, default='pending')
    move_in_date = models.DateField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.booking_id:
            while True:
                new_id = generate_booking_id()
                if not Booking.objects.filter(booking_id=new_id).exists():
                    self.booking_id = new_id
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} booked {self.room.pg_name}"


from django.db import models
from django.utils import timezone


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
