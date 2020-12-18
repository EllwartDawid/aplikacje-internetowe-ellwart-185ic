from rest_framework import viewsets
from . import models
from . import serializers
from .serializers import UserSerializer
from rest_framework import filters
from django.contrib.auth import get_user_model

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

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

def licz(request):  
    html = HttpResponse("")
    if request.COOKIES.get('visits'): 
        #pobieramy liczbe odwiedzin witryny i zapisujemy jako int       
        value = int(request.COOKIES.get('visits'))
        html = HttpResponse("<h1>Witaj! Byłeś tutaj już {} razy!<h1>".format(value + 1))  
        html.set_cookie('visits', value + 1)             
    else:
        value = 1
        html = HttpResponse("<h1>Witaj! Jesteś tu pierwszy raz!<h1>")   
        html.set_cookie('visits', value)        
    return html