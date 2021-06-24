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
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def create(self,request):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         instance = serializer.save()
    #         return Response(instance)


class UserMeView(APIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serilazer_class = UserSerializer
    parser_classes = [JSONParser]

    def get(self,request):
        user = UserSerializer(request.user)
        return Response(user.data)
