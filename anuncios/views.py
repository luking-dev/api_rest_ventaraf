from django.shortcuts import render
from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from anuncios.serializers import AnuncioSerializer
from anuncios.models import Anuncio

class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all().order_by('-fecha')
    serializer_class = AnuncioSerializer
