from django.shortcuts import render
from rest_framework import viewsets
from .models import NoParkingZone
from .serializers import NoParkingZoneSerializer

class NoParkingZoneViewSet(viewsets.ModelViewSet):
    queryset = NoParkingZone.objects.all()
    serializer_class = NoParkingZoneSerializer
