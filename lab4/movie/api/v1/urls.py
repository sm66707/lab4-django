from django.urls import path, include
from .views import hello_drf, movie_home, MovieHome, movie_details, movie_create, movie_update, movie_delete

app_name = 'movie-rest-v1'
urlpatterns = [
    path('hello-drf', hello_drf, name='ho-def'),
    path('', movie_home, name='list'),
    path('generics', MovieHome.as_view(), name='generics-list'),
    path('<int:movie_id>', movie_details, name='details'),
    path('create', movie_create, name='create'),
    path('<int:movie_id>/update', movie_update, name='update'),
    path('<int:movie_id>/delete', movie_delete, name='delete'),
]

