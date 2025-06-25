from django.urls import path

from colleg_project.page import page__web

urlpatterns = [
    path('', page__web.home,name='index'),  # No leading slash

    path('about/', page__web.about, name='about'),
    path('contact/', page__web.contact, name='contact'),
    path('careers/', page__web.career, name='career'),

    #path('room-details/<int:room_id>/', page__web.roomdetails, name='room_details'),
   path('room_booking/<int:room_id>/', page__web.roombooking, name='room_booking'),
    path('booking_success/<int:room_id>/', page__web.booked, name='booking_success'),

]
