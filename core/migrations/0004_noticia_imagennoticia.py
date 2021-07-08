# Generated by Django 3.2.4 on 2021-07-08 04:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_nombrenotica_noticia_nombrenoticia'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagenNoticia',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='imagen de la noticia'),
            preserve_default=False,
        ),
    ]