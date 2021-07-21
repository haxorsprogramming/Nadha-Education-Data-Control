from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection
from django.core import serializers

import datetime

from .models import SiswaData
from app_daerah.models import DaerahKabupaten

waktu = datetime.datetime.now()

# Create your views here.
def tambah_data_proses(request):
    # p_tambah = DataSiswa.objects.create(username='adit',nis='089912',nisn='12221',nama='Aditia Darma',tempat_lahir='Medan',tanggal_lahir=waktu,jenis_kelamin='l',nik='-',alamat='kita',kd_provinsi='1',kd_kabupaten='1',kd_kecamatan='1',kd_desa='1',nama_ibu='s',nama_ayah='1',nama_wali='a',penghasilan_ibu='1',penghasilan_ayah='1',penghasilan_wali='1',update_at=waktu)
    # p_tambah.save();
    context = {
        'status' : 'sukses'
    }
    return JsonResponse(context, safe=False)

def tes_sql_raw(request):
    kabupaten = DaerahKabupaten.objects.all().values()
    kab_data = []
    # print(type(kabupaten))
    no = 0 
    for x in kabupaten:
        nama_kab = x[no]['nama']
        kab_data.append(nama_kab)

    context = {
        'status' : 'sukses',
        'kab_data' : kab_data
    }
    return JsonResponse(context, safe=False)