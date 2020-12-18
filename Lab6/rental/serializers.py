from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Friend
        fields = ('id', 'name')

class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Belonging
        fields = ('id', 'name')

class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Borrowed
        fields = ('id', 'what', 'to_who', 'when', 'returned')

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)

