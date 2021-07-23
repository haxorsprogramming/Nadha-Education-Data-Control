from django.db import models
from datetime import date

# Create your models here.
class PegawaiData(models.Model):
    username = models.CharField(max_length=150, default="NULL")
    nip = models.CharField(max_length=30, default="NULL")
    nuptk = models.CharField(max_length=30, default="NULL")
    nik = models.CharField(max_length=30, default="NULL")
    nama_lengkap = models.CharField(max_length=200, default="NULL")
    jenis_kelamin = models.CharField(max_length=5, default="NULL")
    tanggal_lahir = models.DateField(default=date.today)
    tempat_lahir = models.TextField()
    prov_lahir = models.CharField(max_length=15, default="NULL")
    kab_lahir = models.CharField(max_length=15, default="NULL")
    kec_lahir = models.CharField(max_length=15, default="NULL")
    desa_lahir = models.CharField(max_length=15, default="NULL")
    prov = models.CharField(max_length=15, default="NULL")
    kab = models.CharField(max_length=15, default="NULL")
    kec = models.CharField(max_length=15, default="NULL")
    desa = models.CharField(max_length=15, default="NULL")
    alamat = models.TextField()
    agama = models.CharField(max_length=5, default="NULL")
    gelar = models.CharField(max_length=50, default="NULL")
    tamatan = models.CharField(max_length=200, default="NULL")
    tahun_tamat = models.CharField(max_length=4, default="0000")
    no_ijazah = models.CharField(max_length=50)
    no_hp = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    last_update = models.DateTimeField(auto_now=False)
    class Meta:
        db_table = "tbl_pegawai_data"

class PegawaiJabatan(models.Model):
    username = models.CharField(max_length=150, default="NULL")
    kd_jabatan = models.CharField(max_length=2)
    mulai_menjabat = models.DateField()
    status = models.CharField(max_length=10)
    class Meta:
        db_table = "tbl_pegawai_jabatan"
        
