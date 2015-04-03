# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
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
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('weight', models.IntegerField(default=0, max_length=11)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Modified')),
                ('category', models.ForeignKey(to='pcs.Categories')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('weight', models.IntegerField(default=0, max_length=11)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Modified')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='categories',
            name='page',
            field=models.ForeignKey(to='pcs.Pages'),
            preserve_default=True,
        ),
    ]
