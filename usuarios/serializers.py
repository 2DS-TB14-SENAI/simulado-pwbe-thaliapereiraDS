from rest_framework import serializers
from .models import Usuario

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'telefone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            telefone=validated_data.get('telefone', ''),
            password=validated_data['password']
        )
        return user
