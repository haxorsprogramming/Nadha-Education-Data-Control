from django.contrib import admin
from django.urls import path

from app_auth import views as auth
from app_siswa import views as siswa
from app_pegawai import views as pegawai
from app_sekolah import views as sekolah

urlpatterns = [
    path('', auth.home_page),
]
