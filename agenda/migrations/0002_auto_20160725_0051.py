# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterModelOptions(
            name='contatos',
            options={'verbose_name': 'Contato'},
        ),
        migrations.AlterField(
            model_name='contatos',
            name='operadora',
            field=models.CharField(choices=[(1, 'Vivo'), (2, 'Tim')], max_length=2),
        ),
        migrations.AddField(
            model_name='contatos',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='agenda.Tag'),
        ),
    ]
