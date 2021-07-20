from django.db import models

# Create your models here.
class PpdbRegistrasiSiswa(models.Model):
    username = models.CharField(max_length=150)
    nis = models.CharField(max_length=20)
    nisn = models.CharField(max_length=20)
    nama = models.CharField(max_length=200)
    tempat_lahir = models.TextField()
    tanggal_lahir = models.DateTimeField()
    jenis_kelamin = models.CharField(max_length=1)
    nik = models.CharField(max_length=120)
    alamat = models.TextField()
    kd_provinsi = models.CharField(max_length=3)
    kd_kabupaten = models.CharField(max_length=10)
    kd_kecamatan = models.CharField(max_length=20)
    kd_desa = models.CharField(max_length=30)
    nama_ibu = models.CharField(max_length=200)
    nama_ayah = models.CharField(max_length=200)
    nama_wali = models.CharField(max_length=200)
    penghasilan_ibu = models.CharField(max_length=20)
    penghasilan_ayah = models.CharField(max_length=20)
    penghasilan_wali = models.CharField(max_length=20)
    update_at = models.DateTimeField()
    class Meta:
        db_table = "tbl_ppdb_registrasi_siswa"

class PpdbPeriode(models.Model):
    kd_periode = models.CharField(max_length=20)
    nama_periode = models.CharField(max_length=100)
    keterangan = models.TextField()
    tahun_ajaran_awal = models.CharField(max_length=4)
    tahun_ajaran_akhir = models.CharField(max_length=4)
    mulai_tanggal = models.DateField()
    akhir_tanggal = models.DateField()
    class Meta : 
        db_table = "tbl_ppdb_periode"