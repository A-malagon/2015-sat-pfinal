# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contenidos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=128)),
                ('tipo', models.CharField(max_length=128)),
                ('precio', models.CharField(max_length=128)),
                ('fecha', models.CharField(max_length=128)),
                ('hora', models.CharField(max_length=128)),
                ('fechaFin', models.CharField(max_length=128)),
                ('eventoLargo', models.IntegerField()),
                ('informacion', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FechaActualizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaEleccion', models.CharField(max_length=128)),
                ('contenido', models.ForeignKey(to='cms_content_app.Contenidos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=128)),
                ('nombre', models.CharField(max_length=128)),
                ('comentario', models.CharField(max_length=128)),
                ('actividades', models.ManyToManyField(to='cms_content_app.Contenidos', through='cms_content_app.Membership')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membership',
            name='usuario',
            field=models.ForeignKey(to='cms_content_app.Usuario'),
            preserve_default=True,
        ),
    ]
