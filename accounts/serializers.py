from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models import Q

class UserLoginSerializer(serializers.ModelSerializer):

    token = serializers.CharField(required=False, allow_blank=True, read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('token', 'username', 'email', 'password')
        exra_kwargs = {"password":{"write_only": True}}

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A username or email is required to login")
        user = User.objects.filter(Q(email=email) | Q(username=username)).distinct()

        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        #user.is_active:
        print(user)
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is not valid")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credential please try again")
        data["tokern"] = "Token"
        return data

class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')



