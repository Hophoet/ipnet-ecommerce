from rest_framework import serializers
from .models import Categorie, Produit

class CategorieSerializer(serializers.ModelSerializer):
	"""docstring for EleveSerializer"""
	
	class Meta:
		"""docstring for Meta"""
		model = Categorie
		fields = '__all__'
		

class ProduitSerializer(serializers.ModelSerializer):
	"""docstring for EleveSerializer"""
	
	class Meta:
		"""docstring for Meta"""
		model = Produit
		fields = '__all__'
		