from django.shortcuts import render, redirect
from .models import Reservation
from django.contrib import messages

def index(request):
    return render(request, 'main/index.html')

def reservation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        detail = request.POST.get('detail')

        Reservation.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            detail=detail
        )
        messages.success(request, 'Rezervasyonunuz başarıyla kaydedildi!')
        return redirect('reservation')

    return render(request, 'main/reservation.html')

def menu_view(request):
    return render(request, 'main/menu.html')



def gallery_view(request):
    return render(request, 'main/gallery.html')


