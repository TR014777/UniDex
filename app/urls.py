from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import pokemon_detail


urlpatterns = [
    path('pokemon/<str:name>/', pokemon_detail),
]
