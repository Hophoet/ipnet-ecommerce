from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework import status


from .models import *
from .serializers import PanierSerializer, PanierCreatedSerializer

@api_view(["POST"])
def ajoutPanier(request):
    #
    if request.method == 'POST' :
        serializer = PanierCreatedSerializer(data={'utilisateur' : request.data['utilisateur']['id']})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response({'text': 'Panier non créé'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)



@api_view(["GET", "PUT", 'DELETE'])
def panier(request, id: int):
    try:
        panier: Panier = Panier.objects.get(id=id)
    except Exception as e:
        return Response({'text': 'Panier non trouvé'}, status=status.HTTP_404_NOT_FOUND)
    
    if  request.method == 'GET' :
        return Response(PanierSerializer(panier).data, status.HTTP_200_OK)

    elif request.method == 'PUT' :
        serializer = PanierCreatedSerializer(panier, data={
            'utilisateur' : request.data['utilisateur']['id'],
            'estCommander' : request.data['estCommander']
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({'text': 'Panier non modifié'}, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        panier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)


def ajouterAuPanier(request, id_produit: int, quantite:int = 1):
    
    try:
        # recuperation du produit
        produit = Produit.objects.get(id=id_produit)
    except Exception as exc:
        # Si le produit n'existe pas dans les produits existants
        return Response({'text': 'Produit introuvable'}, status.HTTP_400_BAD_REQUEST)

    # recuperation ou create du produit a commander
    produit_a_commander, produit_a_commander_est_cree = ProduitACommander.objects.get_or_create(
        produit=produit,
        quantite=quantite,
        estCommander=False
    )

    # recuperation ou creation du panier
    panier, panier_est_cree = Panier.objects.get_or_create(
        utilisateur=request.user,
        estCommander=False
    )

    # verification de l'existance du produit_a_commander dans le panier

    if produit_a_commander:
        if panier:
            produit_a_commander_est_contenu_dans_le_panier = produit_a_commander in panier.produitacommander_set.get_queryset()
        else:
            produit_a_commander_est_contenu_dans_le_panier = produit_a_commander in panier_est_cree.produitacommander_set.get_queryset()
    else:
        produit_a_commander_est_contenu_dans_le_panier = produit_a_commander_est_cree in panier.produitacommander_set.get_queryset()


    # produit est contenu dans le panier
    if produit_a_commander_est_contenu_dans_le_panier:
        return Response({'text': 'produit est deja au panier'})

    # produit n'est pas encore dans le panier: lorsque ajouter le au panier
    if panier:
        panier.produitacommander_set.add(produit_a_commander)
    else:
        panier_est_cree.produitacommander_set.add(produit_a_commander)
    return Response({'text': 'produit ajoute avec succes!'})