# Generated by Django 2.2 on 2020-09-08 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20200908_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='game',
            name='tanggal',
            field=models.CharField(max_length=255),
        ),
    ]