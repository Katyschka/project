from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Art
#здесь мы создали классы представлений,

class ArtListView(ListView):
    model=Art
    template_name = 'home.html'

class ArtDetailView(DetailView):
    model=Art
    template_name='detail.html'