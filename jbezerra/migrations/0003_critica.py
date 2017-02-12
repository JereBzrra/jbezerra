# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jbezerra', '0002_delete_critica'),
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
                ('ordem_critico', models.IntegerField()),
            ],
        ),
    ]
