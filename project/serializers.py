
from rest_framework import serializers, fields
from .models import *

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'first_name', 'last_name', 'email', 'team','phone','mobile')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'email','company_name', 'phone', 'mobile', 'sale_contact')

    def create(self, validated_data):

        projet = Client.objects.create( first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        email=validated_data['email'],
                                        phone=validated_data['phone'],
                                        mobile=validated_data['mobile'],
                                        company_name=validated_data['company_name'],
                                        sale_contact_id=self.context['request'].user.id                            
        )

        projet.save()
        return projet

class ContractSerializer(serializers.ModelSerializer):

    payment_due = fields.DateField(input_formats=['%d-%m-%YT%H:%M:%S'])
    
    class Meta:
        model = Contract
        fields = ('id', 'status', 'amount', 'payment_due', 'sale_contact', 'client')
    
    def create(self, validated_data):

        contract = Contract.objects.create( payment_due=validated_data['payment_due'],
                                            amount=validated_data['amount'],
                                            client_id=self.context.get('view').kwargs.get('client_pk'),
                                            sale_contact_id=self.context['request'].user.id                            
        )
        
        contract.save()
        return contract
    

class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ('id', 'atttendees', 'event_date', 'notes', 'support_contact', 'client', 'event_status')
    
    def create(self, validated_data):

        event = Event.objects.create( attendees=validated_data['attendees'],
                                            event_date=validated_data['event_date'],
                                            notes=validated_data['notes'],
                                            client_id=self.context.get('view').kwargs.get('client_pk'),
                                            support_contact_id=self.context['request'].user.id,
                                            event_status_id = validated_data['event_status']                             
        )
        
        event.save()
        return event


class StatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Status
        fields = ('id', 'status')
    
    def create(self, validated_data):
        
        status = Status.objects.create(status=validated_data['status'],
        )
        status.save()
        return status