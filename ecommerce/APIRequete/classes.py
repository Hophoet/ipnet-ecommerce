from django.shortcuts import render
import requests


URL = "http://127.0.0.1:8000/"  #Initialisation du nom du domaine

class GestionProduit:
	"""docstring for GestionProduit"""
	def getProduits():
		"""Méthode pour répérer les produits existants"""
		return requests.get(URL+"api/produits/").json()

	def getProduit(idProduit):
		"""Méthode pour la récupération d'un produit"""
		return requests.get(URL+"api/produit/detail/"+str(idProduit)).json()


class GestionImage:
	"""docstring for GestionImage"""
	def getImages():
		return requests.get(URL+"api/images/").json()
		"""Méthode pour répérer les images existantes"""
	def getImage(idProduit):
		"""Méthode pour la récupération des images d'un produit spécifique"""
		return requests.get(URL+"api/image/detail/"+str(idProduit)).json()


class GestionCategorie:
	"""docstring for GestionCategorie"""
	def getCategorieNom(idCategorie):
		"""Méthode pour la récupération d'une catégorie"""
		return requests.get(URL+"api/categorie/detail/"+str(idCategorie)).json()['nom']

	def getAllCategorie():
		"""Méthode pour répérer les catégories existantes"""
		return requests.get(URL+"api/categories/"+idCategorie).json()
		