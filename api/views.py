from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required


from .models import *
from .serializers import(CategorieSerializer, ProduitSerializer,
                         ImagesSerializer, FournisseurSerializer, CommandeSerializer)


class CategoriesListe(APIView):
    """ recupération de tous les categories disponible """

    def get(self, request, *args, **kwargs):
        """ methode pour la requette get """
        # recuperation de toutes les categories
        categories = Categorie.objects.all()
        categories_serializer = CategorieSerializer(categories, many=True)
        return Response(categories_serializer.data)


class FournisseursListe(APIView):
    """ recupération de tous les categries disponible """

    def get(self, request, *args, **kwargs):
        """ methode pour la requette get """
        # recuperation de tous les fournisseurs
        fournisseurs = Fournisseur.objects.all()
        fournisseurs_serializer = FournisseurSerializer(
            fournisseurs, many=True)
        return Response(fournisseurs_serializer.data, status=status.HTTP_200_OK)


class UtilisateurCommandesListe(APIView):
    """ recupération de tous les commandes d'un utillisateur """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """ methode pour la requette get """
        commandes = Commande.objects.filter(panier__utilisateur=request.user)
        commandes_serializer = CommandeSerializer(commandes, many=True)
        return Response(commandes_serializer.data, status=status.HTTP_200_OK)


class AjoutAuPanierView(APIView):
    """ ajout au panier """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        # recuperation du produit
        produit_id = kwargs.get('produit_id')
        print('produit id', produit_id)
        produit = get_object_or_404(Produit, id=produit_id)
        # recuperation ou create du produit a commander
        produit_a_commander, produit_a_commander_est_cree = ProduitACommander.objects.get_or_create(
            produit=produit,
            utilisateur=request.user,
            quantite=1,
            estCommander=False
        )
        # recuperation ou creation du panier
        panier, panier_est_cree = Panier.objects.get_or_create(
            utilisateur=request.user,
            estCommander=False
        )

        # verification de l'existance du produit_a_commander dans le panier
        produit_a_commander_est_contenu_dans_le_panier = produit_a_commander in panier.produitacommander_set.get_queryset()

        # produit  est contenu dans le panier
        if produit_a_commander_est_contenu_dans_le_panier:
            return Response({'text': 'produit est deja au panier'})
        # produit n'est pas contenu dans le panier
        panier.produitacommander_set.add(produit_a_commander)
        return Response({'text': 'produit ajoute avec succes!'})


class CommanderView(APIView):
    """ ajout au panier """
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        # recuperation ou creation du panier
        panier, panier_est_cree = Panier.objects.get_or_create(
            utilisateur=request.user,
            estCommander=False
        )

        # create livraison
        # make payment
        # create commandes

        return Response({'text': 'pas encore implementer!'})