from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView, UpdateAPIView, ListCreateAPIView
from actor.models import Actor
from .serializers import ActorSerializer, ActorCreateUpdateSerializer

class ActorHome(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorUpdate(UpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

@api_view(['GET'])
def hello_drf(request):
    return Response(data={"message":"Hello"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def actor_home(request):
    actor_object = Actor.objects.all()
    serializer = ActorSerializer(actor_object, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def actor_details(request, actor_id):
    actor = Actor.objects.get(pk=actor_id)
    serializer = ActorSerializer(actor)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def actor_create(request):
    response = {'data':{}, 'status':status.HTTP_400_BAD_REQUEST}
    serializer = ActorCreateUpdateSerializer(data=request.data)
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
def actor_update(request, actor_id):
    response = {'data':{}, 'status':status.HTTP_400_BAD_REQUEST}
    # actor = Actor.objects.filter(pk=actor_id).first()
    actor = Actor.objects.get(pk=actor_id)
    if request.method == 'PUT':
        serializer = ActorCreateUpdateSerializer(instance=actor, data=request.data)
    else:
        serializer = ActorCreateUpdateSerializer(instance=actor, data=request.data, partial=True)
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
def actor_delete(request, actor_id):
    Actor.objects.get(pk=actor_id).delete()
    return Response(data={"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)