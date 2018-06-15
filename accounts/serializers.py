from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserLoginSerializer(serializers.ModelSerializer):

    token = serializers.CharField(required=False, allow_blank=True, read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('token','username', 'email', 'password')
        exra_kwargs = {"password":{"write_only":True}}