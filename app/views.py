from django.shortcuts import render

from app.serializers import CarsSerializer
from .models import Cars
from rest_framework.generics import ListAPIView, CreateAPIView,UpdateAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

class CarsListView(ListAPIView):
    serializer_class = CarsSerializer
    queryset = Cars.objects.all()
    
    
class CarsDetailView(RetrieveAPIView):
    serializer_class = CarsSerializer
    queryset = Cars.objects.all()
    lookup_field = 'pk'
    
    
class CarsCreateView(CreateAPIView):
    serializer_class = CarsSerializer
    queryset = Cars.objects.all()
    
    
class CarsUpdateView(UpdateAPIView):
    serializer_class = CarsSerializer
    queryset = Cars.objects.all()
    lookup_field = 'pk'
    
    
class CarsListCreateView(ListCreateAPIView):
    serializer_class = CarsSerializer
    queryset = Cars.objects.all()
    
    
class CarsUpdateDetailDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarsSerializer
    queryset = Cars.objects.all()
    lookup_field = 'pk'