from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Category

# Create your views here.
class CategoryCreate(CreateView) : 
    model = Category
    fields = "__all__"

    success_url = reverse_lazy('home')