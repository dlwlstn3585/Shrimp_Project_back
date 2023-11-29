from rest_framework import serializers
from .models import ParkingArea

class ParkingAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingArea
        fields = '__all__'
