# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Critica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('fonte', models.CharField(max_length=100)),
                ('critico', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=200)),
                ('critica', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tecnica', models.CharField(max_length=50)),
                ('formato', models.CharField(max_length=20)),
                ('ano', models.IntegerField()),
                ('fase', models.IntegerField()),
                ('colecao', models.BooleanField()),
                ('ativo', models.BooleanField()),
                ('slide', models.BooleanField()),
                ('facebook', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.CharField(max_length=6)),
            ],
        ),
    ]