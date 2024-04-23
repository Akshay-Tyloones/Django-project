from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='guest_name',max_length = 100)
    email = forms.EmailField(label='guest_email')
    reservation_date = forms.DateField(label='Reservation_date')
    guest_number = forms.IntegerField(label='number of guest')

