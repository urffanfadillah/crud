# Generated by Django 2.2.12 on 2020-05-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='tanggal_barang',
            field=models.DateField(),
        ),
    ]
