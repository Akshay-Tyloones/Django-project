from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    
class Reservation(models.Model):
    guest_name = models.CharField(max_length = 100)
    guest_email = models.EmailField()
    reservation_date = models.DateField()
    guest_number = models.IntegerField()
    time = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.guest_name} - {self.reservation_date}"
    
    
class ReservationSettings(models.Model):
    max_guest = models.IntegerField(default = 8)
    max_reservation = models.IntegerField(default = 50)
    
    
    def __str__(self):
        return "reservation setting"
    
    
