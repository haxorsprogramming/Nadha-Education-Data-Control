# Generated by Django 3.2.5 on 2021-07-23 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0004_alter_authuser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='last_login',
            field=models.DateTimeField(),
        ),
    ]