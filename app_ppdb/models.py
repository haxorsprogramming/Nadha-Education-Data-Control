from django.db import models

# Create your models here.
class PpdbPeriode(models.Model):
    kd_periode = models.CharField(max_length=20)
    nama_periode = models.CharField(max_length=200)
    deksripsi = models.TextField()
    kd_tahun_ajaran = models.CharField(max_length=20)
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    biaya_pendaftaran = models.IntegerField()
    aktif = models.CharField(max_length=1)
    class Meta:
        db_table = "tbl_ppdb_periode"

class PpdbJalur(models.Model):
    kd_jalur = models.CharField(max_length=20)
    nama_jalur = models.CharField(max_length=200)
    deksripsi = models.TextField()
    kd_periode = models.CharField(max_length=20)
    kuota = models.IntegerField()
    metode_seleksi = models.CharField(max_length=40)
    aktif = models.CharField(max_length=1)
    class Meta:
        db_table = "tbl_ppdb_jalur"

class PpdbRegistrasi(models.Model):
    kd_registrasi = models.CharField(max_length=25)
    kd_periode = models.CharField(max_length=20)
    kd_jalur = models.CharField(max_length=20)
    kd_jurusan = models.CharField(max_length=20)
    username = models.CharField(max_length=150)
    waktu_daftar = models.DateTimeField()
    status_dokumen = models.CharField(max_length=20)
    status_verifikasi = models.CharField(max_length=20)
    status_pembayaran = models.CharField(max_length=20)
    waktu_verifikasi = models.DateTimeField()
    status_kelulusan = models.CharField(max_length=50)
    username_operator = models.CharField(max_length=150)
    class Meta:
        db_table = "tbl_ppdb_registrasi"

class PpdbVerifikasiDokumen(models.Model):
    kd_dokumen = models.CharField(max_length=20)
    kd_registrasi = models.CharField(max_length=25)
    status_verifikasi = models.CharField(max_length=30)
    alasan_tolak = models.TextField()
    waktu_verifikasi = models.DateTimeField()
    username_verifikator = models.CharField(max_length=150)
    class Meta:
        db_table = "tbl_ppdb_verifikasi_dokumen"

class PpdbNilaiRapor(models.Model):
    kd_registrasi = models.CharField(max_length=25)
    kd_mapel = models.CharField(max_length=20)
    semester = models.IntegerField()
    nilai = models.IntegerField()
    status_verifikasi = models.CharField(max_length=20)
    waktu_verifikasi = models.DateTimeField()
    username_verifikator = models.CharField(max_length=150)
    class Meta:
        db_table = "tbl_ppdb_nilai_rapor"

class PpdbNilaiSertifikat(models.Model):
    kd_registrasi = models.CharField(max_length=25)
    kd_sertifikat = models.CharField(max_length=25)
    nilai = models.IntegerField()
    status_verifikasi = models.DateTimeField()
    waktu_verifikasi = models.DateTimeField()
    username_operator = models.CharField(max_length=150)
    class Meta:
        db_table = "tbl_ppdb_nilai_sertifikat"

class PpdbHasilSeleksi(models.Model):
    kd_registrasi = models.CharField(max_length=25)
    status_seleksi = models.CharField(max_length=20)
    ranking = models.IntegerField()
    waktu_ranking = models.DateTimeField()
    username_operator = models.CharField(max_length=150)
    class Meta:
        db_table = "tbl_ppdb_hasil_seleksi"

class PpdbDataRegistrasi(models.Model):
    username = models.CharField(max_length=150)
    nis = models.CharField(max_length=30)
    nisn = models.CharField(max_length=30)
    nik = models.CharField(max_length=30)
    nama_lengkap = models.CharField(max_length=200)
    jenis_kelamin = models.CharField(max_length=5)
    tanggal_lahir = models.DateField()
    tempat_lahir = models.TextField()
    prov_lahir = models.CharField(max_length=15)
    kab_lahir = models.CharField(max_length=15)
    kec_lahir = models.CharField(max_length=15)
    desa_lahir = models.CharField(max_length=15)
    prov = models.CharField(max_length=15)
    kab = models.CharField(max_length=15)
    kec = models.CharField(max_length=15)
    desa = models.CharField(max_length=15)
    alamat = models.TextField()
    agama = models.CharField(max_length=5)
    golongan_darah = models.CharField(max_length=5)
    berkacamata = models.CharField(max_length=5)
    disabilitas = models.CharField(max_length=30)
    tinggi_badan = models.CharField(max_length=5)
    berat_badan = models.CharField(max_length=5)
    periode_masuk = models.CharField(max_length=20)
    asal_sekolah = models.CharField(max_length=200)
    npsn_asal_sekolah = models.CharField(max_length=40)
    no_ijazah = models.CharField(max_length=40)
    tanggal_lulus = models.DateField()
    no_registrasi_ppdb = models.CharField(max_length=20)
    no_hp = models.CharField(max_length=20)
    email= models.CharField(max_length=150)
    status_orang_tua = models.CharField(max_length=30)
    nama_ayah = models.CharField(max_length=150)
    nama_ibu = models.CharField(max_length=150)
    nama_wali = models.CharField(max_length=150)
    alamat_orang_tua = models.TextField()
    no_hp_orang_tua = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=False)
    class Meta:
        db_table = "tbl_ppdb_data_registrasi"