from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from owner.models import Room, Booking
from dashboard.models import TeamMember
from user.models import ContactDetails


def home(request):
    # Filter parameters
    room_type = request.GET.get('room_type')
    location = request.GET.get('location')

    # Base queryset
    rooms = Room.objects.all()
    if room_type:
        rooms = rooms.filter(room_type=room_type)
    if location:
        rooms = rooms.filter(room_location__icontains=location)

    # Pagination
    paginator = Paginator(rooms, 6)  # Show 6 rooms per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Team members (optional for homepage footer or section)
    member = TeamMember.objects.all()

    return render(request, 'home.html', {
        'room_data': page_obj,
        'member': member
    })



# def roomdetails(request, room_id):
#     room = get_object_or_404(Room, pk=room_id)
#     return render(request, 'room_booking.html', {'room': room})


def roombooking(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request,'room_booking.html', {'room': room})
def about(request):
    return  render(request,'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save to the database
        ContactDetails.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        return render(request, 'contact.html', {
            'success': True,
            'name': name,
            'email': email,
            'message': message
        })

    return render(request, 'contact.html')

job_openings = [
    {
        'job_role': 'Web Developer',
        'job_description': 'Build and maintain websites and web applications.'
    },
    {
        'job_role': 'Frontend Developer',
        'job_description': 'Develop engaging user interfaces using HTML, CSS, and JS frameworks.'
    },
    {
        'job_role': 'Backend Developer',
        'job_description': 'Build robust server-side applications and APIs.'
    },
    {
        'job_role': 'UI/UX Designer',
        'job_description': 'Design user-friendly interfaces and improve user experience.'
    },
    {
        'job_role': 'Content Writer',
        'job_description': 'Create engaging content for web, blogs, and social media.'
    }
]
def career(request):
    return render(request, 'career.html', {'job_openings': job_openings})


#
# def bookroom(request, room_id):
#     return  render(request,'booked_room.html', {'room_id': room_id})

import random
import string
from django.shortcuts import render, get_object_or_404
 # Adjust this import if Room is in another app/module


def generate_booking_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


def booked(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    if request.method == 'POST':
        booking_id = generate_booking_id()

        # Extracting room details
        location = room.room_location
        pg_name = room.pg_name
        pg_owner = room.pg_owner
        room_price = room.room_price
        room_type = room.room_type

        # User-submitted form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')


        context = {
            'booking_id': booking_id,
            'room': room,
            'location': location,
            'pg_name': pg_name,
            'pg_owner': pg_owner,
            'room_price': room_price,
            'room_type': room_type,
            'name': name,
            'email': email,
            'phone': phone,

        }

        return render(request, 'booking_success.html', context)

    return render(request, 'booking_success.html', {'room_id': room_id})
