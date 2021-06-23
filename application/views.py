from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ToDo, User
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins, viewsets


class HomeView(APIView):
    def get(self):
        todos = ToDo.objects.all()
        return Response({"todos": todos})


# class RetrieveUserViewSet():
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def list(self,request):
    #     queryset = self.get_queryset()
    #     serializer = UserSerializer(queryset,many=True)
    #     return Response(serializer.data)
# def getUser(request, pk):
#     tasks = User.objects.get(id=pk)
#     serializer = UserSerializer(tasks, many=False)
#     return Response(serializer.data)
