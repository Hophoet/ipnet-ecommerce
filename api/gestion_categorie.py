from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework import status



from .models import *
from .serializers import CategorieSerializer, CategorieCreatedSerializer

@api_view(["POST"])
def ajoutCategorie(request):
    #{"nom":"categorie2", "description": "Description categorie2", "categorieMere":1}
    if request.method == 'POST' :
        serializer = CategorieCreatedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response({'text': 'Catégorie non créée'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", 'DELETE'])
def categorie(request, id: int):
    try:
        categorie: Categorie = Categorie.objects.get(id=id)
    except Exception as e:
        return Response({'text': 'catégorie non trouvée'}, status=status.HTTP_404_NOT_FOUND)
    
    if  request.method == 'GET' :
        return Response(CategorieSerializer(categorie).data, status.HTTP_200_OK)

    elif request.method == 'PUT' :
        serializer = CategorieCreatedSerializer(categorie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({'text': 'catégorie non modifiée'}, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        categorie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)