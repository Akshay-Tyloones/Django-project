from django.shortcuts import render, HttpResponse
from .models import MenuItem, Reservation, ReservationSettings
from .forms import ContactForm


def home(request):
    return render(request, 'restaurant/home.html')


def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'restaurant/menu.html', {'menu_items' : menu_items})


def reservation(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid(): 
            
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            reservation_date = form.cleaned_data.get('reservation_date')
            guest_number = form.cleaned_data.get('guest_number')
            
            
            settings = ReservationSettings.objects.first() 
            
            
            if guest_number > settings.max_guest:
                return HttpResponse("The number of guests exceeds the allowed limit.")
            
            
            todays_reservation = Reservation.objects.filter(reservation_date=reservation_date).count()
            if todays_reservation >= settings.max_reservation:
                return HttpResponse("Maximum reservations for this date have been reached.")
            

            Reservation.objects.create(
                guest_name=name,
                guest_email=email,
                reservation_date=reservation_date,
                guest_number=guest_number
            )
            return render(request, 'restaurant/reservation_success.html')  
    else:
        form = ContactForm()
    return render(request, 'restaurant/reservationForm.html', {'form': form})

