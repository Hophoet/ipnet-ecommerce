from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework import status



from .models import *
from .serializers import FournisseurSerializer






@api_view(["POST"])
def ajoutFournisseur(request):
    #{"nom":"fournisseur1", "telephone": 978456213, "adresse": "adresse", "email": "email@email.com", "estPerson":false}
    if request.method == 'POST' :
        serializer = FournisseurSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response({'text': 'Fournisseur non créé'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", 'DELETE'])
def fournisseur(request, id: int):
    try:
        fournisseur: Fournisseur = Fournisseur.objects.get(id=id)
    except Exception as e:
        return Response({'text': 'fournisseur non trouvé'}, status=status.HTTP_404_NOT_FOUND)
    
    if  request.method == 'GET' :
        return Response(FournisseurSerializer(fournisseur).data, status.HTTP_200_OK)

    elif request.method == 'PUT' :
        serializer = FournisseurSerializer(fournisseur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({'text': 'fournisseur non modifié'}, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        fournisseur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def fournisseurs(request):
    return Response(FournisseurSerializer(Fournisseur.objects.all(), many=True).data, status.HTTP_200_OK)