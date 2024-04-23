from django.contrib import admin

from django.contrib import admin
from .models import Reservation, ReservationSettings, MenuItem

admin.site.register(MenuItem)
admin.site.register(Reservation)
admin.site.register(ReservationSettings)


