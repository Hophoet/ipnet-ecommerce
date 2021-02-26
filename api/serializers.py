from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	
	class Meta:
		"""docstring for Meta"""
		model = User
		fields = '__all__'

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
	categorieMere = serializers.SerializerMethodField()

	class Meta:
		"""docstring for Meta"""
		model = Categorie
		fields = '__all__'

	def get_categorieMere(self, obj):
		if obj.categorieMere is not None:
			return CategorieSerializer(obj.categorieMere).data
		else:
			return None
		
class CategorieCreatedSerializer(serializers.ModelSerializer):


	class Meta:
		"""docstring for Meta"""
		model = Categorie
		fields = '__all__'
		
class ProduitSerializer(serializers.ModelSerializer):
	categories = CategorieSerializer(many=True, read_only=True)
	fournisseur = FournisseurSerializer(many=False, read_only=True)
	class Meta:
		"""docstring for Meta"""
		model = Produit
		fields = '__all__'

class ProduitCreatedSerializer(serializers.ModelSerializer):
	class Meta:
		"""docstring for Meta"""
		model = Produit
		fields = '__all__'

class ProduitACommanderSerializer(serializers.ModelSerializer):
	
	class Meta:
		"""docstring for Meta"""
		model = ProduitACommander
		fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
	
	class Meta:
		"""docstring for Meta"""
		model = Image
		fields = '__all__'

class PanierSerializer(serializers.ModelSerializer):
	
	class Meta:
		"""docstring for Meta"""
		model = Panier
		fields = '__all__'
class PanierCreatedSerializer(serializers.ModelSerializer):
	
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
