from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import generics

from .models import VladExelModels
from .serializers import VladExelSerializers

class VladExelAPIView(generics.CreateAPIView):
    serializer_class = VladExelSerializers
    queryset = VladExelModels.objects.all()

