from django.urls import path, include
from .views import actors_list, actor_details, actor_create, actor_delete, actor_update

app_name = 'actor'
urlpatterns = [
    path('list', actors_list, name='list'),
    path('create', actor_create, name='create'),
    path('details/<int:pk>', actor_details, name='details'),
    path('update/<int:pk>',actor_update, name='update'),
    path('delete/<int:pk>', actor_delete, name='delete'),
]