from django.db import models

# Create your models here.
class DataMasterTahunAjaran(models.Model):
    kd_tahun_ajaran = models.CharField(max_length=10)
    nama_tahun_ajaran = models.CharField(max_length=150)
    mulai_tanggal = models.DateField()
    akhir_tanggal = models.DateField()
    status = models.DateField()
    aktif = models.CharField(max_length=1)
    class Meta:
        db_table = "tbl_data_master_tahun_ajaran"

class DataMasterJurusan(models.Model):
    kd_jurusan = models.CharField(max_length=20)
    nama_jurusan = models.CharField(max_length=100)
    deksripsi = models.TextField()
    aktif = models.CharField(max_length=1)
    class Meta:
        db_table = "tbl_data_master_jurusan"

class DataMasterRombel(models.Model):
    kd_rombel = models.CharField(max_length=30)
    nama_rombel = models.CharField(max_length=100)
    deksripsi = models.TextField()
    kd_jurusan = models.CharField(max_length=20)
    kd_semester = models.CharField(max_length=20)
    jam_belajar = models.CharField(max_length=20)
    aktif = models.CharField(max_length=1)
    class Meta:
        db_table = "tbl_data_master_rombel"

class DataMasterSemester(models.Model):
    kd_semester = models.CharField(max_length=20)
    nama = models.CharField(max_length=100)
    kd_tahun_ajaran = models.CharField(max_length=10)
    mulai_tanggal = models.DateField()
    akhir_tanggal = models.DateField()
    status = models.CharField(max_length=20)
    aktif = models.CharField(max_length=1)
    class Meta:
        db_table = "tbl_data_master_semester"

class DataMasterRuangan(models.Model):
    kd_ruangan = models.CharField(max_length=20)
    nama_ruangan =  models.CharField(max_length=200)
    tipe =  models.CharField(max_length=30)
    kapasitas =  models.CharField(max_length=3)
    status =  models.CharField(max_length=30)
    fasilitas = models.TextField()
    aktif = models.CharField(max_length=1)
    class Meta:
        db_table = "tbl_data_master_ruangan"

class DataMasterEkstrakurikuler(models.Model):
    kd_ekskul = models.CharField(max_length=10)
    nama = models.CharField(max_length=100)
    deksripsi = models.TextField()
    aktif = models.CharField(max_length=1)
    class Meta:
        db_table = "tbl_data_master_ekstrakurikuler"

class DataMasterInventori(models.Model):
    kd_barang = models.CharField(max_length=25)
    nama_barang = models.CharField(max_length=200)
    deksripsi = models.TextField()
    kd_ruangan = models.CharField(max_length=20)
    kondisi = models.CharField(max_length=20)
    qt = models.CharField(max_length=5)
    kategori = models.CharField(max_length=50)
    aktif = models.CharField(max_length=1)
    class Meta:
        db_table = "tbl_data_master_inventori"

class DataMasterMataPelajaran(models.Model):
    kd_mapel = models.CharField(max_length=20)
    nama_mapel = models.CharField(max_length=200)
    deksripsi = models.TextField()
    tipe = models.CharField(max_length=30)
    aktif = models.CharField(max_length=1)
    class Meta:
        db_table = "tbl_data_master_mata_pelajaran"

class DataMasterMataSekolah(models.Model):
    kd_data = models.CharField(max_length=20)
    nama = models.CharField(max_length=100)
    deksripsi = models.TextField()
    nilai = models.TextField()
    class Meta:
        db_table = "tbl_data_master_sekolah"