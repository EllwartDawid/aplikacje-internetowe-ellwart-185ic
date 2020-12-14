
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    #metadane modelu
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post

