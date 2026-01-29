from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking

def home(request):
    return render(request, 'home.html')

def create_booking(request):
    if request.method == 'POST':
        booking = Booking.objects.create(
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            pet_type=request.POST.get('pet_type'),
            number_of_pets=request.POST.get('number_of_pets'),
            duration=request.POST.get('duration'),
            address=request.POST.get('address'),
            special_instructions=request.POST.get('special_instructions'),
        )

        # Email to user
        send_mail(
            subject='Pet Care Request Received 🐾',
            message=(
                f"Hi {booking.full_name},\n\n"
                "We have received your pet care request.\n"
                "Our team will contact you shortly.\n\n"
                "Thank you for trusting us!"
            ),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[booking.email],
        )

        # Email to admin
        send_mail(
            subject='New Pet Care Booking',
            message=(
                f"New booking received:\n\n"
                f"Name: {booking.full_name}\n"
                f"Phone: {booking.phone}\n"
                f"Pet: {booking.pet_type}\n"
                f"Duration: {booking.duration}"
            ),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['petcare.service@gmail.com'],
        )

        return redirect('bookings:success')

    return render(request, 'booking_form.html')

def success(request):
    return render(request, 'success.html')
