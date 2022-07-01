from django.urls import path, include
from .views import movies_list, movie_details, movie_create, movie_delete, movie_update

app_name = 'movie'
urlpatterns = [
    path('list', movies_list, name='list'),
    path('create', movie_create, name='create'),
    path('details/<int:pk>', movie_details, name='details'),
    path('update/<int:pk>',movie_update, name='update'),
    path('delete/<int:pk>', movie_delete, name='delete'),
]

