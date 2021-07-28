from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework import generics, permissions
from .permissions import *

# Create your views here.



# Project
class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticated, IsSaleTeam|IsStaff)

    def get_queryset(self):
        return Client.objects.all()

class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = (permissions.IsAuthenticated, IsSaleTeam|IsStaff)

    def get_queryset(self):
        return Contract.objects.all()

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated, IsSupportTeam)

    def get_queryset(self):
        return Event.objects.all()


class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Status.objects.all()