from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework import generics, permissions
# from .permissions import 

# Create your views here.



# Project
class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Client.objects.all()