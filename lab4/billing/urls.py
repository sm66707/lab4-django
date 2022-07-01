from django.urls import path, include
from .views import billing_list, billing_details, billing_create, billing_delete, billing_edit, billing_update

app_name = 'billing'
urlpatterns = [
    path('list', billing_list, name='list'),
    path('create>', billing_create, name='create'),
    path('details/<str:billing_name>', billing_details, name='details'),
    path('edit/<str:billing_name>', billing_edit, name='edit'),
    path('update/<str:billing_name>',billing_update, name='update'),
    path('delete/<str:billing_name>', billing_delete, name='delete'),
]

