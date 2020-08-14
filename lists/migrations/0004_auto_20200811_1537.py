# Generated by Django 3.1 on 2020-08-11 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_auto_20200811_1144'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0003_auto_20200811_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='rooms',
            field=models.ManyToManyField(blank=True, related_name='lists', to='rooms.Room'),
        ),
        migrations.AlterField(
            model_name='list',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to=settings.AUTH_USER_MODEL),
        ),
    ]