from django.db import models

# Create your models here.
class PembelajaranJadwalMataPelajaran(models.Model):
    kd_jadwal_pelajaran = models.CharField(max_length=20)
    kd_mapel = models.CharField(max_length=20)
    kd_rombel = models.CharField(max_length=30)
    kd_guru = models.CharField(max_length=150)
    hari = models.CharField(max_length=1)
    mulai = models.DateTimeField()
    selesai = models.DateTimeField()
    urutan = models.IntegerField()
    aktif = models.CharField(max_length=1)
    class Meta:
        db_table = "tbl_pembelajaran_jadwal_mata_pelajaran"

class PembelajaranJamBelajar(models.Model):
    token_jam_belajar = models.CharField(max_length=50)
    kd_jadwal_pelajaran = models.CharField(max_length=20)
    kd_ruangan = models.CharField(max_length=20)
    token_absensi = models.CharField(max_length=8)
    dimulai = models.DateTimeField()
    selesai = models.DateTimeField()
    total_hadir = models.IntegerField()
    class Meta:
        db_table = "tbl_pembelajaran_jam_belajar"
        
class PembelajaranRuangAbsensi(models.Model):
    token_jam_belajar = models.CharField(max_length=50)
    username_guru = models.CharField(max_length=150)
    username_siswa = models.CharField(max_length=150)
    hadir = models.IntegerField()
    izin = models.IntegerField()
    tanpa_keterangan = models.IntegerField()
    sakit = models.IntegerField()
    total = models.IntegerField()
    class Meta:
        db_table = "tbl_pembelajaran_ruang_absensi"

class PembelajaranAbsensiSiswa(models.Model):
    token_jam_belajar = models.CharField(max_length=50)
    username_siswa = models.CharField(max_length=150)
    waktu_absen = models.DateTimeField()
    terlambat = models.CharField(max_length=1)
    class Meta:
        db_table = "tbl_pembelajaran_absensi_siswa"

class PembelajaranAbsensiGuru(models.Model):
    token_jam_belajar = models.CharField(max_length=50)
    username_guru = models.CharField(max_length=150)
    waktu_absen = models.DateTimeField()
    terlambat = models.CharField(max_length=1)
    class Meta:
        db_table = "tbl_pembelajaran_absensi_guru"