
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from pets.models import Pet, Appointment
from .forms import *


class PetsPageTest(TestCase):
    def test_pets_page(self):
        #Logging in
        user = User.objects.create_user(username='jon', password='password')
        self.client.login(username='jon', password='password')

        Pet.objects.create(pet_name='Ghost', species='Dog', breed='Great Dane', weight_in_pounds=10, Owner=user)

        response = self.client.get('/pets/')
        #Checking if the page loaded
        self.assertEqual(response.status_code, 200)
        get_response = self.client.get(reverse('pets'))
        #Seeing if the owner exists on the page
        self.assertContains(get_response, 'jon')

class PetsDetailPageTest(TestCase):
    def test_pets_page(self):
        #Logging in
        user = User.objects.create_user(username='jon', password='password')
        self.client.login(username='jon', password='password')

        Pet.objects.create(pet_name='Ghost', species='Dog', breed='Great Dane', weight_in_pounds=10, Owner=user)
        pet = Pet.objects.get(pet_name='Ghost')
        Appointment.objects.create(date_of_appointment='2020-05-08', duration_minutes=50, special_instructions='None', pet=pet)

        response = self.client.get('/pet/1')
        #Checking if the page loaded
        self.assertEqual(response.status_code, 200)
        #Checking the pet's details
        self.assertContains(response, 'Dog')

class PetCreationPageTest(TestCase):
    def test_submit_question_creation_form(self):
            #Logging in
            user = User.objects.create_user(username='jon', password='password')
            self.client.login(username='jon', password='password')
            #Post Request
            response = self.client.post('/pet/create/',
                {
                    'pet_name': 'Bayone',
                    'species': 'Dog',
                    'breed': 'Jack Russell',
                    'weight_in_pounds': 5,
                    'Owner': user,
                })
            #Seeing if the response was successful
            self.assertEqual(response.status_code, 302)
            #Checking that the data was updated in the database
            new_pet = Pet.objects.filter(pet_name='Bayone')
            self.assertTrue(new_pet.exists())

class PetCreationPageTest(TestCase):
    def test_submit_question_creation_form(self):
            #Logging in
            user = User.objects.create_user(username='jon', password='password')
            self.client.login(username='jon', password='password')
            #Creating a pet
            pet = Pet.objects.create(pet_name='Ghost', species='Dog', breed='Great Dane', weight_in_pounds=10, Owner=user)

            #Post Request
            response = self.client.post('/appointment/create/',
                {
                    'date_of_appointment': '2020-05-08',
                    'duration_minutes': 45,
                    'special_instructions': 'None',
                    'pet': pet,
                })
            #Seeing if the response was successful
            self.assertEqual(response.status_code, 302)
            #Checking that the data was updated in the database
            new_appointment = Appointment.objects.filter(date_of_appointment='2020-05-08')
            self.assertTrue(new_appointment.exists())
