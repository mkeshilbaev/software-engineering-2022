from rest_framework import serializers

from .models import Service


class MicroServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class RequestSerializer(serializers.Serializer):
    method = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
