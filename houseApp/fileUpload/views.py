from django.shortcuts import render
from rest_framework import generics, views, viewsets
from fileUpload.models import House
from fileUpload.serializer import HouseSerializer


class HouseViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing, retrieving and updating house information.
    """
    serializer_class = HouseSerializer
    queryset = House.objects.all()
