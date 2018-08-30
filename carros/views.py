from rest_framework import viewsets
from .serializers import CarSerializer

class CarSetView(viewsets.ModelViewSet):

    queryset = Car.objects.all()
    Serializer_class = 
