
from rest_framework import serializers
from .models import *

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'first_name', 'last_name', 'email', 'team','phone','mobile')

# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Staff
#         fields = ('id', 'first_name', 'last_name', 'email', 'team','phone','mobile')
#         extra_kwargs = {'password': {'write_only': True}}
        
#     def create(self, validated_data):
#         user = Staff.objects.create(
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             team=validated_data['team'],
#             phone=validated_data['phone'],
#             mobile=validated_data['mobile'],
#         )
#         user.set_password(validated_data['password'])
#         user.save()

#         return user
    
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
    class Meta:
        model = Contract
        fields = ('id', 'status', 'amount', 'payement_due', 'sale_contact', 'client')


class EventSerializer(serializers.ModelSerializer):
    pass