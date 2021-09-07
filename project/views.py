from django.shortcuts import render
from django_filters.filters import CharFilter, DateFilter, DateFromToRangeFilter, RangeFilter
from rest_framework.fields import DateField
from .serializers import *
from rest_framework import viewsets
from rest_framework import generics, permissions
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

# Create your views here.

# Filter


class ContractFilter(filters.FilterSet):
    amount_exact = CharFilter(field_name='amount', lookup_expr='exact')
    amount = RangeFilter()
    payment_due_exact = DateFilter(field_name="payment_due", lookup_expr="date")
    payment_due = DateFromToRangeFilter()
    client = CharFilter(field_name='client__email', lookup_expr='exact')
    sale_contact = CharFilter(field_name='sale_contact__email', lookup_expr='exact')

    class Meta:
        model = Contract
        fields = ['status', 'amount', 'payment_due', 'client', 'sale_contact', 'amount_exact', 'payment_due_exact']


class EventFilter(filters.FilterSet):
    attendees_exact = CharFilter(field_name='attendees', lookup_expr='exact')
    attendees = RangeFilter()
    event_date_exact = DateFilter(field_name="event_date", lookup_expr="date")
    event_date = DateFromToRangeFilter()
    client = CharFilter(field_name='client__email', lookup_expr='exact')
    support_contact = CharFilter(field_name='support_contact__email', lookup_expr='exact')
    event_status = CharFilter(field_name='event_status__status', lookup_expr='exact')

    class Meta:
        model = Event
        fields = ['attendees', 'event_date', 'client', 'event_status', 'support_contact']


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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def get_queryset(self):
        return Status.objects.all()
