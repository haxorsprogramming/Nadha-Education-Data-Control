from django.db import models

# Create your models here.
class DaerahKabupaten(models.Model):
    id_kab = models.CharField(max_length=4)
    id_prov = models.CharField(max_length=2)
    nama = models.CharField(max_length=200)
    id_jenis = models.IntegerField()
    class Meta:
        db_table = "tbl_kabupaten"