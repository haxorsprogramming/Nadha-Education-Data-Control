from django.db import models

# Create your models here.
class KeuanganPembayaranSpp(models.Model):
    kd_token = models.CharField(max_length=50)
    username_operator = models.CharField(max_length=150)
    tipe_pembayaran = models.CharField(max_length=50)
    jumlah_biaya = models.IntegerField()
    total_pembayaran = models.IntegerField()
    waktu_pembayaran = models.DateTimeField()
    class Meta:
        db_table = "tbl_keuangan_pembayaran_spp"

class KeuanganTagihanSpp(models.Model):
    kd_token = models.CharField(max_length=50)
    kd_tahun_ajaran = models.CharField(max_length=20)
    kd_semester = models.CharField(max_length=25)
    kd_periode_pembayaran = models.CharField(max_length=20)
    total_tagihan = models.IntegerField()
    username_siswa = models.CharField(max_length=150)
    waktu_pembayaran = models.DateTimeField()
    status_pembayaran = models.CharField(max_length=20)
    username_operator = models.CharField(max_length=150)
    class Meta:
        db_table = "tbl_keuangan_tagihan_spp"

class KeuanganPengeluaranSekolah(models.Model):
    kd_pengeluaran = models.CharField(max_length=20)
    nama_pengeluaran = models.CharField(max_length=200)
    deksripsi = models.TextChoices()
    kategori = models.CharField(max_length=50)
    total_pengeluaran = models.IntegerField()
    username_operator = models.CharField(max_length=150)
    waktu_transaksi = models.DateTimeField()
    class Meta:
        db_table = "tbl_keuangan_pengeluaran_sekolah"

class KeuanganPembayaranRegistrasiPpdb(models.Model):
    kd_registrasi = models.CharField(max_length=50)
    metode_pembayaran = models.CharField(max_length=30)
    token_pembayaran = models.CharField(max_length=35)
    jumlah_pembayaran = models.IntegerField()
    waktu_pembayaran = models.DateTimeField()
    username_operator = models.CharField(max_length=150)
    class Meta:
        db_table = "tbl_keuangan_pembayaran_registrasi_ppdb"

class KeuanganPeriodePembayaran(models.Model):
    kd_periode_pembayaran = models.CharField(max_length=50)
    kd_tahun_ajaran = models.CharField(max_length=25)
    kd_semester = models.CharField(max_length=20)
    bulan = models.CharField(max_length=2)
    mulai_periode = models.DateField()
    akhir_periode = models.DateField()
    aktif = models.CharField(max_length=1)
    class Meta:
        db_table = "tbl_keuangan_periode_pembayaran"    
