from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150)
    kata_sandi = models.CharField(max_length=200)
    tipe_user = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = "tbl_user"