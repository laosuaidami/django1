# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0002_auto_20180318_0552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodsinfo',
            old_name='gtype',
            new_name='classify',
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gadv',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gbrief',
            field=models.CharField(max_length=200, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gclick',
            field=models.IntegerField(verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gcontent',
            field=tinymce.models.HTMLField(verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe7\xae\x80\xe7\xbb\x8d'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(upload_to=b'df_goods', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gprice',
            field=models.DecimalField(verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gstocks',
            field=models.IntegerField(verbose_name=b'\xe5\xba\x93\xe5\xad\x98\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtitle',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gunit',
            field=models.CharField(default=b'500g', max_length=20, verbose_name=b'\xe5\x8d\x95\xe4\xbb\xb7'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='isDelete',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x88\xa0\xe9\x99\xa4'),
        ),
        migrations.AlterField(
            model_name='typeinfo',
            name='isDelete',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x88\xa0\xe9\x99\xa4'),
        ),
        migrations.AlterField(
            model_name='typeinfo',
            name='ttitle',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
