from rest_framework import serializers
from actor.models import Actor

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'gender']

class ActorCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Actor