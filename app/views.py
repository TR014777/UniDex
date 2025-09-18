from .serializers import PokemonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

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
