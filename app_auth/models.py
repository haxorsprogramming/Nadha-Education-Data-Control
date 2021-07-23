from NadhaEducationDataControl.settings import USE_TZ
from django.db import models
from datetime import date, datetime
from django.utils.timezone import is_naive, timezone
import time

# Create your models here.
class AuthUser(models.Model):
    username = models.CharField(max_length=150)
    kata_sandi = models.CharField(max_length=200)
    tipe_user = models.CharField(max_length=30)
    login_last = models.DateTimeField(auto_now=True)
    aktif = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = "tbl_auth_user"

class AuthSekolah(models.Model):
    kd_access = models.CharField(max_length=50)
    secret_key = models.CharField(max_length=25)
    npsn = models.CharField(max_length=20)
    nama_sekolah = models.CharField(max_length=200)
    email_sekolah = models.CharField(max_length=200)
    class Meta:
        db_table = "tbl_auth_sekolah"

class AuthRegistrasiUser(models.Model):
    username = models.CharField(max_length=150)
    kata_sandi = models.CharField(max_length=150)
    tipe_user = models.CharField(max_length=30)
    waktu_registrasi = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "tbl_auth_registrasi_siswa"

class AuthLogLogin(models.Model):
    username = models.CharField(max_length=150)
    waktu_login = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(max_length=50)
    user_agent = models.TextField()
    class Meta:
        db_table = "tbl_auth_log_login"