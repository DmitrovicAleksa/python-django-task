from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ToDo

class HomeView(APIView):
    def get(self,request):
        todos = ToDo.objects.all()
        return Response({"todos" : todos})
