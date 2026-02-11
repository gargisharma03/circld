from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Interest
from .serializers import InterestSerializer

# List all interests or create a new one
class InterestListView(generics.ListCreateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

# Retrieve, update, or delete a specific interest
class InterestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
