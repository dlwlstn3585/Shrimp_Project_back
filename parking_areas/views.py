from django.shortcuts import render
from rest_framework import viewsets
from .models import ParkingArea
from .serializers import ParkingAreaSerializer

class ParkingAreaViewSet(viewsets.ModelViewSet):
    queryset = ParkingArea.objects.all()
    serializer_class = ParkingAreaSerializer
