
from django.urls import path
from .views import * 

urlpatterns = [
    path('',index, name="index"),
    path('search/',search_songs, name='search_songs'),
]
