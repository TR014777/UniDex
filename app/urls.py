from django.urls import path
from . import views

urlpatterns = [
    path('', views.resgatar_pokemon, name='resgatar_pokemon'),
    path('api/pokemon/<str:name>/', views.pokemon_detail, name='pokemon_detail'),
]

