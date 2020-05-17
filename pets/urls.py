from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pet/create/', views.pet_create, name='pet-create-page'),
    path('appointment/create/', views.appointment_create, name='appointment-create-page'),
    path('pets/', views.pets, name="pets"),
    path('one_pet/<int:pet_id>', views.one_pet, name="pet"),
    path('calendar/', views.calendar, name="calendar")
]
