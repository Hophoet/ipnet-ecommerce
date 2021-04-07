from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework import status



from .models import *
from .serializers import ProduitSerializer, ProduitCreatedSerializer





@api_view(["POST"])
def ajoutProduit(request):
    #{"nom":"produit7", "prix": 32000,"caracteristique": "Les caracterique", "quantite": 100, "categories": [1], "fournisseur":1}
    if request.method == 'POST' :
        produit = ProduitCreatedSerializer(data={
            'nom' : request.data['nom'],
            'prix' : request.data['prix'],
            'diminu_price' : request.data['diminu_price'],
            'caracteristique' : request.data['caracteristique'],
            'quantite' : request.data['quantite'],
            'categories' : request.data['categories']['id'],
            'fournisseur' : request.data['fournisseur']['id'],
        })
        if produit.is_valid():
            produit.save()
            return Response(produit.data, status.HTTP_201_CREATED)
        else:
            return Response({'text': 'produit non créé'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", 'DELETE'])
def produit(request, id: int):
    try:
        produit: Produit = Produit.objects.get(id=id)
    except Exception as e:
        return Response({'text': 'produit non trouvé'}, status=status.HTTP_404_NOT_FOUND)
    
    if  request.method == 'GET' :
        return Response(ProduitSerializer(produit).data, status.HTTP_200_OK)

    elif request.method == 'PUT' :
        serializer = ProduitCreatedSerializer(produit, data={
            'nom' : request.data['nom'],
            'prix' : request.data['prix'],
            'diminu_price' : request.data['diminu_price'],
            'caracteristique' : request.data['caracteristique'],
            'quantite' : request.data['quantite'],
            'categories' : request.data['categories']['id'],
            'fournisseur' : request.data['fournisseur']['id'],
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({'text': 'produit non modifié'}, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        produit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def produits(request):
    return Response(ProduitSerializer(Produit.objects.all(), many=True).data, status.HTTP_200_OK)