
from django.shortcuts import render, HttpResponse
from .forms import ContactForm




def dashboard(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
                  
    else:
        form = ContactForm()
    return render(request, 'dashboard.html',{'form':form})











