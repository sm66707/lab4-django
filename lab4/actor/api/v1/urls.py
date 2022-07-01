from django.urls import path, include
from .views import hello_drf, actor_home, ActorHome, actor_details, actor_create, actor_update, actor_delete

app_name = 'actor-rest-v1'
urlpatterns = [
    path('hello-drf', hello_drf, name='ho-def'),
    path('', actor_home, name='list'),
    path('generics', ActorHome.as_view(), name='generics-list'),
    path('<int:actor_id>', actor_details, name='details'),
    path('create', actor_create, name='create'),
    path('<int:actor_id>/update', actor_update, name='update'),
    path('<int:actor_id>/delete', actor_delete, name='delete'),
]

