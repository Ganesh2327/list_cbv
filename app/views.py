from django.shortcuts import render
from django.views.generic import ListView
from app.models import *
# Create your views here.


class trainer_list(ListView):
    model= trainer
    template_name='trainer_list.html'
    context_object_name='tl'
    ordering=['trainer_name']



