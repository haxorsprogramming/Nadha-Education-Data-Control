# Generated by Django 3.2.5 on 2021-07-23 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PegawaiData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='NULL', max_length=150)),
                ('nip', models.CharField(default='NULL', max_length=30)),
                ('nuptk', models.CharField(default='NULL', max_length=30)),
                ('nik', models.CharField(default='NULL', max_length=30)),
                ('nama_lengkap', models.CharField(default='NULL', max_length=200)),
                ('jenis_kelamin', models.CharField(default='NULL', max_length=5)),
                ('tanggal_lahir', models.DateField(default=datetime.date.today)),
                ('tempat_lahir', models.TextField()),
                ('prov_lahir', models.CharField(default='NULL', max_length=15)),
                ('kab_lahir', models.CharField(default='NULL', max_length=15)),
                ('kec_lahir', models.CharField(default='NULL', max_length=15)),
                ('desa_lahir', models.CharField(default='NULL', max_length=15)),
                ('prov', models.CharField(default='NULL', max_length=15)),
                ('kab', models.CharField(default='NULL', max_length=15)),
                ('kec', models.CharField(default='NULL', max_length=15)),
                ('desa', models.CharField(default='NULL', max_length=15)),
                ('alamat', models.TextField()),
                ('agama', models.CharField(default='NULL', max_length=5)),
                ('gelar', models.CharField(default='NULL', max_length=50)),
                ('tamatan', models.CharField(default='NULL', max_length=200)),
                ('tahun_tamat', models.CharField(default='0000', max_length=4)),
                ('no_ijazah', models.CharField(max_length=50)),
                ('no_hp', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'tbl_pegawai_data',
            },
        ),
        migrations.CreateModel(
            name='PegawaiJabatan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='NULL', max_length=150)),
                ('kd_jabatan', models.CharField(max_length=2)),
                ('mulai_menjabat', models.DateField()),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tbl_pegawai_jabatan',
            },
        ),
    ]
