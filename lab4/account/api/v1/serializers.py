from asyncore import write
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        fields = ('username', 'email', 'password', 'password_confirm', 'first_name', 'last_name', 'date_of_birth')
        model = User
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {'required': True},
            "date_of_birth": {'required': True},
        }
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already exists')
        if not value:
            raise serializers.ValidationError('Email is required')
        return value
    def save(self, **kwargs):
        user = User(
            username=self.validated_data.get('username'),
        )
        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError('Password and password confirm must match')
        user.set_password(self.validated_data.get('password'))
        user.save()
        return user