from django.contrib import admin
from django.conf.urls import url
from .views import UserLoginAPIView

app_name = 'accounts'
urlpatterns = [
    url(r'^$', UserLoginAPIView.as_view(), name="login"),

]