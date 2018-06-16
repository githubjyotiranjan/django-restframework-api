from django.contrib import admin
from django.conf.urls import url
from .views import UserLoginAPIView,UserDetailsAPIView

app_name = 'accounts'
urlpatterns = [
    url(r'^login/$', UserLoginAPIView.as_view(), name="login"),
    url(r'^userdetails/$', UserDetailsAPIView.as_view(), name="login"),
]