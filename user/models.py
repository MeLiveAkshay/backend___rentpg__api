from django.db import models
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


class BookingDetails(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)

    check_in = models.DateField()
    check_out = models.DateField()
    booked_on = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking #{self.booking_id} - {self.customer_name}"