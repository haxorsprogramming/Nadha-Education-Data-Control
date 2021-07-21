from django.db import models

# model siswa.
class SiswaData(models.Model):
    username = models.CharField(max_length=150)
    nis = models.CharField(max_length=20)
    nisn = models.CharField(max_length=20)
    nik = models.CharField(max_length=120)
    nama_lengkap = models.CharField(max_length=200)
    jenis_kelamin = models.CharField(max_length=1)
    tanggal_lahir = models.DateTimeField()
    tempat_lahir = models.TextField()
    kd_provinsi = models.CharField(max_length=3)
    kd_kabupaten = models.CharField(max_length=10)
    kd_kecamatan = models.CharField(max_length=20)
    kd_desa = models.CharField(max_length=30)
    alamat = models.TextField()
    nama_ibu = models.CharField(max_length=200)
    nama_ayah = models.CharField(max_length=200)
    nama_wali = models.CharField(max_length=200)
    penghasilan_ibu = models.CharField(max_length=20)
    penghasilan_ayah = models.CharField(max_length=20)
    penghasilan_wali = models.CharField(max_length=20)
    update_at = models.DateTimeField()
    class Meta:
        db_table = "tbl_siswa_data"