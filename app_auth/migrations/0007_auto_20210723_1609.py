# Generated by Django 3.2.5 on 2021-07-23 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0006_rename_last_login_authuser_login_last'),
    ]

    operations = [
        migrations.AddField(
            model_name='authregistrasiuser',
            name='waktu_registrasi',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='authloglogin',
            name='waktu_login',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='login_last',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
