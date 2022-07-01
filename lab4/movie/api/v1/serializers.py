from rest_framework import serializers
from movie.models import Movie
from actor.api.v1.serializers import ActorSerializer

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    class Meta:
        fields = '__all__'
        model = Movie
        depth = 1

class MovieCreateSerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        if value.lower() == 'movie':
            raise serializers.ValidationError('Movie name cannot be movie')
        return value

    def validate(self, attrs):
        # if attrs['name'].lower() == 'movie':
        #     raise serializers.ValidationError('Movie name cannot be movie')
        return attrs

    class Meta:
        fields = '__all__'
        model = Movie

class MovieUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Movie