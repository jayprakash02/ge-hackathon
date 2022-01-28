from rest_framework import serializers
from .models import User, PrivateData


class PrivateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateData
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    data = PrivateDataSerializer(many=False, read_only=False)

    class Meta:
        model = User
        fields = ["username", "data","public_key","verifying_key"]
