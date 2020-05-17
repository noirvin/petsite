from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pet, Appointment
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import PetForm, AppointmentForm


def home(request):
    return render(request, 'home.html')
