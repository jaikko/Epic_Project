from rest_framework import serializers, fields
from .models import *


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'first_name', 'last_name', 'email', 'team', 'phone', 'mobile')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'email', 'company_name', 'phone', 'mobile', 'sale_contact')

    def create(self, validated_data):

        projet = Client.objects.create(first_name=validated_data['first_name'],
                                       last_name=validated_data['last_name'],
                                       email=validated_data['email'],
                                       phone=validated_data['phone'],
                                       mobile=validated_data['mobile'],
                                       company_name=validated_data['company_name'],
                                       sale_contact_id=self.context['request'].user.id)

        projet.save()
        return projet


class ContractSerializer(serializers.ModelSerializer):

    payment_due = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S'])

    class Meta:
        model = Contract
        fields = ('id', 'status', 'amount', 'payment_due', 'sale_contact', 'client')

    def create(self, validated_data):

        contract = Contract.objects.create(payment_due=validated_data['payment_due'],
                                           amount=validated_data['amount'],
                                           client_id=self.context.get('view').kwargs.get('client_pk'),
                                           sale_contact_id=self.context['request'].user.id)

        contract.save()
        return contract


class EventSerializer(serializers.ModelSerializer):

    event_date = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S'])
    # event_date = fields.DateField(format="%d-%m-%Y")

    class Meta:
        model = Event
        fields = ('id', 'attendees', 'event_date', 'notes', 'support_contact', 'client', 'event_status', 'contract')

    def create(self, validated_data):
        id = self.context.get('view').kwargs.get('contract_pk')
        record = Event.objects.filter(contract_id=id).first()
        if record:
            raise serializers.ValidationError({"detail": "A event already existed for this contract"})

        event = Event.objects.create(attendees=validated_data['attendees'],
                                     event_date=validated_data['event_date'],
                                     notes=validated_data['notes'],
                                     client_id=self.context.get('view').kwargs.get('client_pk'),
                                     support_contact_id=self.context['request'].user.id,
                                     event_status_id=validated_data['event_status'].id,
                                     contract_id=self.context.get('view').kwargs.get('contract_pk'))

        event.save()
        return event


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('id', 'status')

    def create(self, validated_data):

        status = Status.objects.create(status=validated_data['status'])
        status.save()
        return status
