from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Pokemon
from .serializers import PokemonSerializer


def home(request):
    return HttpResponse("Olá, mundo! Página inicial do app.")

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer