# Generated by Django 3.2.5 on 2021-07-24 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthLogLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('waktu_login', models.DateTimeField(auto_now=True)),
                ('ip_address', models.CharField(max_length=50)),
                ('user_agent', models.TextField()),
            ],
            options={
                'db_table': 'tbl_auth_log_login',
            },
        ),
        migrations.CreateModel(
            name='AuthRegistrasiUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('kata_sandi', models.CharField(max_length=150)),
                ('tipe_user', models.CharField(max_length=30)),
                ('waktu_registrasi', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tbl_auth_registrasi_siswa',
            },
        ),
        migrations.CreateModel(
            name='AuthSekolah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kd_access', models.CharField(max_length=50)),
                ('secret_key', models.CharField(max_length=25)),
                ('npsn', models.CharField(max_length=20)),
                ('nama_sekolah', models.CharField(max_length=200)),
                ('email_sekolah', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tbl_auth_sekolah',
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('kata_sandi', models.CharField(max_length=200)),
                ('tipe_user', models.CharField(max_length=30)),
                ('login_last', models.DateTimeField()),
                ('aktif', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'tbl_auth_user',
            },
        ),
    ]
