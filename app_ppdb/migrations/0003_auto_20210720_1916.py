# Generated by Django 3.2.5 on 2021-07-20 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_ppdb', '0002_dataperiodeppdb'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DataPeriodePpdb',
            new_name='PpdbPeriode',
        ),
        migrations.RenameModel(
            old_name='DataRegistrasiPpdb',
            new_name='PpdbRegistrasiSiswa',
        ),
        migrations.AlterModelTable(
            name='ppdbperiode',
            table='tbl_ppdb_periode',
        ),
        migrations.AlterModelTable(
            name='ppdbregistrasisiswa',
            table='tbl_ppdb_registrasi_siswa',
        ),
    ]