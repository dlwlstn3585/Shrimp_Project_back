from rest_framework import serializers
from .models import NoParkingZone

class NoParkingZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoParkingZone
        fields = '__all__'
