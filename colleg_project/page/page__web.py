from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from owner.models import Room
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


def book_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'booking_form.html', {
        'room': room
    })



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