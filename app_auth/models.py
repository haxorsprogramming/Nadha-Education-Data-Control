from django.db import models
from django.utils.timezone import timezone

# Create your models here.
class AuthUser(models.Model):
    username = models.CharField(max_length=150)
    kata_sandi = models.CharField(max_length=200)
    tipe_user = models.CharField(max_length=30)
    last_login = models.DateTimeField()
    active = models.CharField(max_length=1)
    class Meta:
        db_table = "tbl_auth_user"

class AuthRegistrasiUser(models.Model):
    username = models.CharField(max_length=150)
    kata_sandi = models.CharField(max_length=150)
    tipe_user = models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_auth_registrasi_sekolah"

class AuthSekolah(models.Model):
    kd_access = models.CharField(max_length=50)
    secret_key = models.CharField(max_length=25)
    npsn = models.CharField(max_length=20)
    nama_sekolah = models.CharField(max_length=200)
    email_sekolah = models.CharField(max_length=200)
    start_subs = models.DateField()
    expired_subs = models.DateField()
    class Meta:
        db_table = "tbl_auth_sekolah"