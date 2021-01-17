from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from .models import *
from .serializers import CategorieSerializer, ProduitSerializer, ImagesSerializer


class CategoriesListe(APIView):
    """ recupération de tous les categories disponible """

    def get(self, request, *args, **kwargs):
        """ get methode requeste """
        # recuperation de toutes les categories
        categories = Categorie.objects.all()
        categories_serializer = CategorieSerializer(categories, many=True)
        return Response(categories_serializer.data)
