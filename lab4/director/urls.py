from django.urls import path, include
from .views import directors_list, director_details, director_create, director_delete, director_update

app_name = 'director'
urlpatterns = [
    path('list', directors_list, name='list'),
    path('create', director_create, name='create'),
    path('details/<int:pk>', director_details, name='details'),
    path('update/<int:pk>',director_update, name='update'),
    path('delete/<int:pk>', director_delete, name='delete'),
]

