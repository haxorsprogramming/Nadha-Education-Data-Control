# Generated by Django 3.2.5 on 2021-07-23 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0005_alter_authuser_last_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authuser',
            old_name='last_login',
            new_name='login_last',
        ),
    ]
