from rest_framework import serializers
from .models import ClientModel

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__' 
        

class ClientLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    
class NewClientSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    phone_number = serializers.CharField()
    NIDA_id_number = serializers.CharField()
    password = serializers.CharField()