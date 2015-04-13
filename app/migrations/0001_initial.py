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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('weight', models.IntegerField(default=0, max_length=11)),
                ('endMessage', models.TextField(blank=True, default='')),
                ('showHeading', models.BooleanField(default=False)),
                ('heading1', models.CharField(blank=True, max_length=10)),
                ('heading2', models.CharField(blank=True, max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Modified')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price1', models.FloatField(blank=True, default=0.0)),
                ('price2', models.FloatField(blank=True, default=0.0)),
                ('weight', models.IntegerField(default=0, max_length=11)),
                ('isVegan', models.BooleanField(default=False)),
                ('isVegtarian', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Modified')),
                ('category', models.ForeignKey(to='app.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('weight', models.IntegerField(default=0, max_length=11)),
                ('endMessage', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Modified')),
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
