from django.contrib import admin
from django.urls import path

from app_auth import views as auth

urlpatterns = [
    path('', auth.home_page),
]
