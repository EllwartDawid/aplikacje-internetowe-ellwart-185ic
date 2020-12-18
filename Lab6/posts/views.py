from rest_framework import viewsets
from rest_framework import generics, permissions
from .models import Post
from django.shortcuts import render
from .permissions import IsAuthorOrReadOnly 
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model
from datetime import datetime
from django.http import HttpResponse

class PostViewSet(viewsets.ModelViewSet): 
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    #serializer
    serializer_class = PostSerializer

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