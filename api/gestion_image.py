''' from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ImagesSerializerOperation



@api_view(['PUT'])  # On oublie pas de mettre en PUT
@parser_classes((MultiPartParser,))
@permission_classes((permissions.IsAuthenticated,))
@csrf_exempt
def upload_document(request):
    s = ImagesSerializerOperation(data=request.data)
    if s.is_valid():
        s.save(profile=request.user)  # C'est ici que l'on ajoute l'utilisateur
        return Response({'detail': s.data})
    return Response({'detail': s.errors}, status=status.HTTP_400_BAD_REQUEST)

permissions. '''

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import ImagesSerializerOperation, ImagesSerializerReturn
from .models import Produit, Image


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        image_serializer = ImagesSerializerOperation(data={
            'image' : request.data['image'],
            'produit' : int(request.GET.get('id'))
        })

        if image_serializer.is_valid():
            image_serializer.save()
            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(["GET"])
def images_produit(request, id: int):
    
    try:
        images: Image = Produit.objects.get(id=id).get_images()
    except Exception as e:
        return Response([{
            'produit': 0,
            'image': '/media/default.jpg'
            }], status.HTTP_200_OK)
    
    if  request.method == 'GET' :
        if not images:
            return Response([{
                'produit': 0,
                'image': '/media/default.jpg'
                }], status.HTTP_200_OK)
        return Response(ImagesSerializerReturn(images, many=True).data, status.HTTP_200_OK)


@api_view(["GET"])
def image_produit(request, id: int):
    try:
        image: Image = Produit.objects.get(id=id).get_images()[0]
    except Exception as e:
        return Response({
            'produit': 0,
            'image': '/media/default.jpg'
            }, status.HTTP_200_OK)
    
    if  request.method == 'GET' :
        if not image:
            return Response({
                'produit': 0,
                'image': '/media/default.jpg'
                }, status.HTTP_200_OK)
        return Response(ImagesSerializerReturn(image).data, status.HTTP_200_OK)

