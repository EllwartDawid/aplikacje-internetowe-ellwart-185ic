from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters

class FriendViewset(viewsets.ModelViewSet):
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer
    #SeatchFilter umożliwia wyszukiwanie
    #OrderingFilter umożliwia filtracje np roznąco lub malejąco
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']

class BelongingViewset(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer

class BorrowedViewset(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer