from urllib import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
# from rest_framework.generics import ListAPIView, UpdateAPIView
# from movie.models import Movie
from .serializers import UserSerializer

@api_view(['POST'])
@permission_classes([])
def signup(request):
    response = {'data':{}, 'status':status.HTTP_400_BAD_REQUEST}
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_201_CREATED
    else:
        response['data'] = serializer.errors
    return Response(**response)

class logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)