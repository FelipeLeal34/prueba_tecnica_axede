from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    hoteles = Hotel.objects.all()
    print(hoteles)
    return render(request, "index.html", {'hoteles' : hoteles})


def Bogota(request):
    habitaciones = Habitacion.objects.filter(hotel = 1)
    return render(request, "Bogota.html", {'habitaciones' : habitaciones})


def Barranquilla(request):
    habitaciones = Habitacion.objects.filter(hotel = 4)
    return render(request, "Barranquilla.html", {'habitaciones' : habitaciones})


def Cali(request):
    habitaciones = Habitacion.objects.filter(hotel = 2)
    return render(request, "Cali.html", {'habitaciones' : habitaciones})

def Cartagena(request):
    habitaciones = Habitacion.objects.filter(hotel = 3)
    return render(request, "Cartagena.html" , {'habitaciones' : habitaciones})




# Bogota = 1
# Barranquilla = 2
# Cali = 3
# Cartagena = 4