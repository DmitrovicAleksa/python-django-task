from django.db.models import query
from django.http import request
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ToDo, User
from .serializers import UserSerializer
from rest_framework import mixins, viewsets
from rest_framework import authentication, permissions
from rest_framework.parsers import JSONParser
from .permissions import AdminAccessPermission


class HomeView(APIView):
    def get(self):
        todos = ToDo.objects.all()
        return Response({"todos": todos})


class UsersViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminAccessPermission]



class UserMeView(APIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serilazer_class = UserSerializer

    def get(self, request):
        user = UserSerializer(request.user)
        return Response(user.data)
