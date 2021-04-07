from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework import status


from django.contrib.auth.models import User
from .models import *
from .serializers import UtilisateurSerializer, UserSerializer


@api_view(["POST"])
def ajoutUtilisateur(request):
    if request.method == 'POST' :
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response({'text': 'Utilisateur non créé'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", 'DELETE'])
def utilisateur(request, id: int):
    try:
        utilisateur: User = User.objects.get(id=id)
    except Exception as e:
        return Response({'text': 'Utilisateur non trouvé'}, status=status.HTTP_404_NOT_FOUND)
    
    if  request.method == 'GET' :
        return Response(UserSerializer(utilisateur).data, status.HTTP_200_OK)

    elif request.method == 'PUT' :
        serializer = UserSerializer(utilisateur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({'text': 'Utilisateur non modifié'}, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        utilisateur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)
