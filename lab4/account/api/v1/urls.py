from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import signup, logout

app_name = 'account-rest-v1'
urlpatterns = [
    path('rest-login', obtain_auth_token),
    path('rest-signup', signup, name='signup'),
    path('rest-logout', logout.as_view(), name='logout'),
]

