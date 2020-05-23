from django.shortcuts import render
from django.contrib import messages

from .models import Car
# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from Cars.models import Car

class CarList(ListView):
    model = Car

class CarView(DetailView):
    model = Car

class CarCreate(CreateView):
    model = Car
    fields = ['name']
    success_url = reverse_lazy('car_list')    

class CarUpdate(UpdateView):
    model = Car
    fields = ['name']
    success_url = reverse_lazy('car_list')

class CarDelete(DeleteView):
    model = Car
    success_url = reverse_lazy('car_list')