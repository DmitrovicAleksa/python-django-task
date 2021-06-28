from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ToDo, User
from .serializers import UserSerializer
from rest_framework import  viewsets
from rest_framework import  permissions
from .permissions import AdminAccessPermission
from rest_framework.filters import SearchFilter
from django.shortcuts import render


class HomeView(APIView):
    def get(self):
        todos = ToDo.objects.all()
        return Response({"todos": todos})



def getUserTemplate(response,id):
        user = User.objects.get(pk = id)
        return render(response,'user.html',{"user":user})


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminAccessPermission]

    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name']



class UserMeView(APIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serilazer_class = UserSerializer

    def get(self, request):
        user = UserSerializer(request.user)
        return Response(user.data)
