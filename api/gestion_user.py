from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, UserRegisterSerializer, LoginSerializer, UserRegisterSerializerSuper
from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication

class RegisterUserApi(generics.GenericAPIView):
    serializer_class = UserRegisterSerializerSuper

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        #, context = self.serializer_context()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            "token" : token
        })

class LoginUserApi(generics.GenericAPIView):
    #permission_classes = ()
    authentication_classes = ()
    permission_classes = ()
    #authentication_classes = [BasicAuthentication, ]
    #permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = LoginSerializer
    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        #, context = self.serializer_context()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            "token" : token
        })

class UserReturnApi(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user