from django.contrib import admin
from .models import Friend, Belonging, Borrowed

#Dodajemy tutaj nasze Posty do panelu administracynego, by móc je tam zobaczyć
admin.site.register(Friend)
admin.site.register(Belonging)
admin.site.register(Borrowed)