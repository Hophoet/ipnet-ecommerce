from rest_framework import generics, permissions
from rest_framework.response import Response
#from knox.models import AuthToken
from .serializers import UserSerializer, UserRegisterSerializer, LoginSerializer

class RegisterUserApi(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user" : UserSerializer(user, context = self.serializer_context()).data
            #"token" : AuthToken.objects.create(user)
        })

class LoginUserApi(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        return Response({
            "user" : UserSerializer(user, context = self.serializer_context()).data
            #"token" : AuthToken.objects.create(user)
        })

class UserReturnApi(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user