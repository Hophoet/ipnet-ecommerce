from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from .models import *
from .serializers import CategorieSerializer, ProduitSerializer


#Gestion des catégories

@api_view(['GET'])
def listeCategories(request):
	'''Fonction pour lister les catégories'''
	categories = Categorie.objects.all()
	serializer = CategorieSerializer(categories, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def enregistrerCategorie(request):
	'''Fonction pour ajouter une catégorie'''
	if request.method == 'POST':
		
		serializer = CategorieSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	

#Gestion des Produits

@api_view(['GET'])
def listeProduits(request):
	'''Fonction pour lister les Produits'''
	produits = Produit.objects.all()
	serializer = ProduitSerializer(produits, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def detailProduit(request, id):
	'''Fonction pour le detail d'un produit'''
	try:
		produit = Produit.objects.get(id=id)
	except Exception as e:
		return Response(status=status.HTTP_404_NOT_FOUND)
	serializer = ProduitSerializer(produit)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def enregistrerProduit(request):
	'''Fonction pour ajouter un produit'''
	if request.method == 'POST':
		#data = JsonParser().parser(request)
		serializer = ProduitSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	