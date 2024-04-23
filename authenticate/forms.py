# from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'profile_picture', 'bio')
        # fields = ('__all__')