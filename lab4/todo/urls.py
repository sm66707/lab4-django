from django.urls import path, include
from .views import todo_details, todo_home, todo_delete, todo_edit, todo_done, todo_undone, todo_update

app_name = 'todo'
urlpatterns = [
    path('', todo_home, name='home'),
    path('details/<str:todo_name>', todo_details, name='details'),
    path('edit/<str:todo_name>', todo_edit, name='edit'),
    path('update/<str:todo_name>',todo_update, name='update'),
    path('done/<str:todo_name>', todo_done, name='done'),
    path('undone/<str:todo_name>', todo_undone, name='undone'),
    path('delete/<str:todo_name>', todo_delete, name='delete'),
]

