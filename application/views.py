from django.db.models import query
from django.http import request
from rest_framework import views
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ToDo, User
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins, viewsets
from rest_framework import authentication, permissions
from rest_framework.parsers import JSONParser
import json



class HomeView(APIView):
    def get(self):
        todos = ToDo.objects.all()
        return Response({"todos": todos})


class UsersViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAdminUser)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(APIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = (permissions.IsAdminUser)
    serilazer_class = UserSerializer
    parser_classes = [JSONParser]

    def get(self,request):
        user = UserSerializer(request.user)
        return Response(user.data)

class UserMeView(APIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serilazer_class = UserSerializer
    parser_classes = [JSONParser]

    def get(self,request):
        user = UserSerializer(request.user)
        return Response(user.data)


