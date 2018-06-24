from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserLoginSerializer,UserDetailSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout

class UserLoginAPIView(APIView):
    """
    Creates the user.
    """

    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    def post(self, request, format='json'):

        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token, create = Token.objects.get_or_create(user=user)
            print(token)
            return Response({"token":token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #     new_data = serializer.data
        #     return Response(new_data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserLoginAPIView(APIView):
#     """
#     Creates the user.
#     """
#
#     permission_classes = [AllowAny]
#     serializer_class = UserLoginSerializer
#     def post(self, request, format='json'):
#
#         data = request.data
#         serializer = UserLoginSerializer(data=data)
#         if serializer.is_valid():
#             user = serializer.validated_data['user']
#             login(request, user)
#             token, create = Token.object.get_or_create(user=user)
#             return Response({"token":token.key}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailsAPIView(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserLoginSerializer
    def get(self, request, format=None):
        

        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)