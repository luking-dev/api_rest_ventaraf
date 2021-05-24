from rest_framework import serializers
from anuncios.models import Anuncio

class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = '__all__'
        extra_kwargs = {'id': {'required': False}}
