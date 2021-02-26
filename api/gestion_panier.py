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
        serializer = PanierCreatedSerializer(data=request.data)
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
        serializer = PanierCreatedSerializer(panier, data=request.data)
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
