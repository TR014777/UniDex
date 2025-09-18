from rest_framework import serializers

class PokemonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    height = serializers.IntegerField()
    weight = serializers.IntegerField()
    types = serializers.ListField(child=serializers.CharField())
    image = serializers.URLField()
