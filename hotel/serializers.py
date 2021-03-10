from abc import ABC

from rest_framework import serializers


class CheapestHotelSerializer(serializers.Serializer):
    input = serializers.JSONField(required=True)

