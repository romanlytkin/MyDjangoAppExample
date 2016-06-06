# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city_name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('lname', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('comment', models.CharField(max_length=160)),
                ('city', models.ForeignKey(to='app.City')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region_name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='RegionCity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.ForeignKey(to='app.City')),
                ('region', models.ForeignKey(to='app.Region')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='region',
            field=models.ForeignKey(to='app.Region'),
        ),
    ]
