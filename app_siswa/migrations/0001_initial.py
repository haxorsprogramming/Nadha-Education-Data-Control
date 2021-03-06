# Generated by Django 3.2.5 on 2021-07-24 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiswaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('nis', models.CharField(max_length=30)),
                ('nisn', models.CharField(max_length=30)),
                ('nik', models.CharField(max_length=30)),
                ('nama_lengkap', models.CharField(max_length=200)),
                ('jenis_kelamin', models.CharField(max_length=5)),
                ('tanggal_lahir', models.DateField()),
                ('tempat_lahir', models.TextField()),
                ('prov_lahir', models.CharField(max_length=15)),
                ('kab_lahir', models.CharField(max_length=15)),
                ('kec_lahir', models.CharField(max_length=15)),
                ('desa_lahir', models.CharField(max_length=15)),
                ('prov', models.CharField(max_length=15)),
                ('kab', models.CharField(max_length=15)),
                ('kec', models.CharField(max_length=15)),
                ('desa', models.CharField(max_length=15)),
                ('alamat', models.TextField()),
                ('agama', models.CharField(max_length=5)),
                ('golongan_darah', models.CharField(max_length=5)),
                ('berkacamata', models.CharField(max_length=5)),
                ('disabilitas', models.CharField(max_length=30)),
                ('tinggi_badan', models.CharField(max_length=5)),
                ('berat_badan', models.CharField(max_length=5)),
                ('periode_masuk', models.CharField(max_length=20)),
                ('asal_sekolah', models.CharField(max_length=200)),
                ('npsn_asal_sekolah', models.CharField(max_length=40)),
                ('no_ijazah', models.CharField(max_length=40)),
                ('tanggal_lulus', models.DateField()),
                ('no_registrasi_ppdb', models.CharField(max_length=20)),
                ('no_hp', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=150)),
                ('status_orang_tua', models.CharField(max_length=30)),
                ('nama_ayah', models.CharField(max_length=150)),
                ('nama_ibu', models.CharField(max_length=150)),
                ('nama_wali', models.CharField(max_length=150)),
                ('alamat_orang_tua', models.TextField()),
                ('no_hp_orang_tua', models.CharField(max_length=20)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'tbl_siswa_data',
            },
        ),
    ]
