from .serializers import PokemonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import requests


def resgatar_pokemon(request):
    name = request.GET.get("name")  # pega o nome enviado no input
    pokemon_data = None
    error = None

    if name:  # só busca se o usuário digitou algo
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            error = "Pokémon não encontrado."
            return render(request, 'erro.html')
        else:
            data = response.json()
            pokemon_data = {
                "id": data["id"],
                "name": data["name"],
                "height": data["height"],
                "weight": data["weight"],
                "types": [t["type"]["name"] for t in data["types"]],
                "image": data["sprites"]["front_default"]
            }

    return render(request, "form.html", {"pokemon": pokemon_data, "error": error})

@api_view(['GET'])
def pokemon_detail(request, name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return Response({"error": "Pokémon não encontrado"}, status=404)
    
    data = response.json()
    
    pokemon_data = {
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]],
        "image": data["sprites"]["front_default"]
    }
    
    serializer = PokemonSerializer(pokemon_data)
    return Response(serializer.data)
