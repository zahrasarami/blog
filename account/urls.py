from django.contrib import admin
from django.urls import path
from account.views import Registerview

urlpatterns = [
    path('register/' , Registerview.as_view())
]