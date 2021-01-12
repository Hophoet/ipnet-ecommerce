from rest_framework import serializers
from .models import *


class UtilisateurSerializer(serializers.ModelSerializer):
	
	class Meta:
		"""docstring for Meta"""
		model = Utilisateur
		fields = '__all__'

class FournisseurSerializer(serializers.ModelSerializer):
	
	class Meta:
		"""docstring for Meta"""
		model = Fournisseur
		fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
	
	class Meta:
		"""docstring for Meta"""
		model = Categorie
		fields = '__all__'
		

class ProduitSerializer(serializers.ModelSerializer):
	
	class Meta:
		"""docstring for Meta"""
		model = Produit
		fields = '__all__'
		
class ProduitCommanderSerializer(serializers.ModelSerializer):
	
	class Meta:
		"""docstring for Meta"""
		model = ProduitCommander
		fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
	
	class Meta:
		"""docstring for Meta"""
		model = Images
		fields = '__all__'

class PanierSerializer(serializers.ModelSerializer):
	
	class Meta:
		"""docstring for Meta"""
		model = Panier
		fields = '__all__'


class CommandeSerializer(serializers.ModelSerializer):
	
	class Meta:
		"""docstring for Meta"""
		model = Commande
		fields = '__all__'

class LivraisonSerializer(serializers.ModelSerializer):
	
	class Meta:
		"""docstring for Meta"""
		model = Livraison
		fields = '__all__'