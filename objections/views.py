from rest_framework import viewsets
from .models import TownshipObjection, FarmObjection
from .serializers import TownshipObjectionSerializer, FarmObjectionSerializer


class TownshipObjectionViewSet(viewsets.ModelViewSet):
    queryset = TownshipObjection.objects.all()
    serializer_class = TownshipObjectionSerializer


class FarmObjectionViewSet(viewsets.ModelViewSet):
    queryset = FarmObjection.objects.all()
    serializer_class = FarmObjectionSerializer