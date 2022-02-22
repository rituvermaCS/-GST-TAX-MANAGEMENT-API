from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import login
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, UpdateUserSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class UpdateProfileView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UpdateUserSerializer

@api_view(['DELETE'])
def userDelete(request, pk):
    profile = User.objects.get(id = pk)
    profile.delete()
    return Response("Profile deleted successfully.")


@api_view(['GET','POST'])
def userList(request):
    if request.method == 'GET':
        profile = User.objects.all()
        serializer = UserSerializer(profile, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        serializer = UserSerializer(data = jsonData)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data)
        else:
           return JsonResponse(serializer.errors)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a single user as per user request.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj


