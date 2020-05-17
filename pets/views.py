
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pet, Appointment
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import PetForm, AppointmentForm


def home(request):
    return render(request, 'home.html')

def pets(request):
  context = {
    'pets': Pet.objects.filter()
  }
  return render(request, 'pets.html', context)

def one_pet(request, pet_id):
    context = {
    'pet': Pet.objects.get(id=pet_id),
    'appointments' : Appointment.objects.filter(pet=pet_id).order_by('date_of_appointment')
    }
    return render(request, 'pet.html', context)

def calendar(request):
  context = {
    'appointments': Appointment.objects.order_by('date_of_appointment')
  }
  return render(request, 'calendar.html', context)


def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pets')
    else:
        form = PetForm()
    return render(request,
                  'create_pet.html',
                  {
                      'form': form
                  })

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/calender')
    else:
        form = AppointmentForm()
    return render(request,
                  'create_appointment.html',
                  {
                      'form': form
                  })
