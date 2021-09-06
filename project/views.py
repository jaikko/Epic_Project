from django.shortcuts import render
from django_filters.filters import DateFromToRangeFilter, RangeFilter
from .serializers import *
from rest_framework import viewsets
from rest_framework import generics, permissions
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

# Create your views here.

# Filter


class ContractFilter(filters.FilterSet):
    amount = RangeFilter()
    payment_due = DateFromToRangeFilter()

    class Meta:
        model = Contract
        fields = ['status', 'amount', 'payment_due']


class EventFilter(filters.FilterSet):
    attendees = RangeFilter()
    event_date = DateFromToRangeFilter()

    class Meta:
        model = Event
        fields = ['attendees', 'event_date']


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticated, IsSaleTeam | IsStaff)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name']

    def get_queryset(self):
        return Client.objects.all()


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = (permissions.IsAuthenticated, IsSaleTeam | IsStaff)
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContractFilter

    def get_queryset(self):
        return Contract.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated, EventAcces | IsSupportTeam)
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter

    def get_queryset(self):
        return Event.objects.all()


class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Status.objects.all()
