
from django.forms import ModelForm
from .models import Pet, Appointment

class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['pet_name', 'species', 'breed', 'weight_in_pounds', 'Owner']

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['date_of_appointment', 'duration_minutes', 'special_instructions', 'pet']
