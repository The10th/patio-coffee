# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('weight', models.IntegerField(default=0, max_length=11)),
                ('created_at', models.DateTimeField(verbose_name='Created', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Modified', auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField()),
                ('weight', models.IntegerField(default=0, max_length=11)),
                ('created_at', models.DateTimeField(verbose_name='Created', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Modified', auto_now_add=True)),
                ('category', models.ForeignKey(to='app.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('weight', models.IntegerField(default=0, max_length=11)),
                ('created_at', models.DateTimeField(verbose_name='Created', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Modified', auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='category',
            name='page',
            field=models.ForeignKey(to='app.Page'),
            preserve_default=True,
        ),
    ]
