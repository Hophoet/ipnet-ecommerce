from django.shortcuts import render

from .APIRequete.classes import GestionProduit, GestionImage, GestionCategorie
def accueil(request):
	produits = [] #Initialisation de la liste des produits à vide
	for produit in GestionProduit.getProduits(): #Parourir les produit
		"""Changer ID des catégories par leur nom spécifique car dans le rendu c'est juste son ID qui est envoyé"""
		produit['categorie'] = GestionCategorie.getCategorieNom(produit['categorie']) #Changement fait
		produits.append(produit) #Ajout du produit modifié à la liste créée

	return render(request, 'index.html', 
		{'produits' : produits, 'images' : GestionImage.getImages()}
		)