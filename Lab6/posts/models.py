from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    #jeden autor może mić dużo postów 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #stringi z maksymalną długością 50
    title = models.CharField(max_length=50)
    #pole tekstowe
    body = models.TextField()
    #data utworzenia
    created_at = models.DateTimeField(auto_now_add=True)
    #data zaktualizowania
    updated_at = models.DateTimeField(auto_now=True)

    #wyświetla w panelu administratora tytuł
    def __str__(self):
        return self.title

