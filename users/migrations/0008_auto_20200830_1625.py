# Generated by Django 3.1 on 2020-08-30 20:25

import core.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200823_1200'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', core.managers.CustomUserManager()),
            ],
        ),
    ]