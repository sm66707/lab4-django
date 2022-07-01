from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView, UpdateAPIView, ListCreateAPIView
from movie.models import Movie
from .serializers import MovieSerializer, MovieCreateSerializer, MovieUpdateSerializer
from .permissions import MyPermission

class MovieHome(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieUpdate(UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

@api_view(['GET'])
def hello_drf(request):
    return Response(data={"message":"Hello"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_home(request):
    movie_object = Movie.objects.all()
    serializer = MovieSerializer(movie_object, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_details(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def movie_create(request):
    response = {'data':{}, 'status':status.HTTP_400_BAD_REQUEST}
    serializer = MovieCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_201_CREATED
        # return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    else:
        response['data'] = serializer.errors
    return Response(**response)
    # return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','PATCH'])
def movie_update(request, movie_id):
    response = {'data':{}, 'status':status.HTTP_400_BAD_REQUEST}
    # movie = Movie.objects.filter(pk=movie_id).first()
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'PUT':
        serializer = MovieUpdateSerializer(instance=movie, data=request.data)
    else:
        serializer = MovieUpdateSerializer(instance=movie, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_201_CREATED
    else:
        response['data'] = serializer.errors
    return Response(**response)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_delete(request, movie_id):
    Movie.objects.get(pk=movie_id).delete()
    return Response(data={"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)