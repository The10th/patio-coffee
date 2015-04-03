# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('weight', models.IntegerField(default=0, max_length=11)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('weight', models.IntegerField(default=0, max_length=11)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Modified')),
                ('category', models.ForeignKey(to='pcs.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('weight', models.IntegerField(default=0, max_length=11)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Modified')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='categories',
            name='page',
        ),
        migrations.RemoveField(
            model_name='items',
            name='category',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='Items',
        ),
        migrations.DeleteModel(
            name='Pages',
        ),
        migrations.AddField(
            model_name='category',
            name='page',
            field=models.ForeignKey(to='pcs.Page'),
            preserve_default=True,
        ),
    ]
