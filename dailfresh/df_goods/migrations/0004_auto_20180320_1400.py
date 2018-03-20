# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0003_auto_20180318_1646'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsinfo',
            options={'verbose_name': '\u5546\u54c1\u4fe1\u606f', 'verbose_name_plural': '\u5546\u54c1\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='typeinfo',
            options={'verbose_name': '\u5546\u54c1\u5206\u7c7b', 'verbose_name_plural': '\u5546\u54c1\u5206\u7c7b'},
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gadv',
            field=models.BooleanField(default=False, verbose_name='\u5e7f\u544a'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gbrief',
            field=models.CharField(max_length=200, verbose_name='\u7b80\u4ecb'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gclick',
            field=models.IntegerField(verbose_name='\u70b9\u51fb\u91cf'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gcontent',
            field=tinymce.models.HTMLField(verbose_name='\u8be6\u7ec6\u7b80\u7ecd'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(upload_to='df_goods', verbose_name='\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gprice',
            field=models.DecimalField(verbose_name='\u4ef7\u683c', max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gstocks',
            field=models.IntegerField(verbose_name='\u5e93\u5b58\u91cf'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtitle',
            field=models.CharField(max_length=20, verbose_name='\u5546\u54c1\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gunit',
            field=models.CharField(default='500g', max_length=20, verbose_name='\u5355\u4f4d'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='isDelete',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664'),
        ),
        migrations.AlterField(
            model_name='typeinfo',
            name='isDelete',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664'),
        ),
        migrations.AlterField(
            model_name='typeinfo',
            name='ttitle',
            field=models.CharField(max_length=20, verbose_name='\u5206\u7c7b\u540d\u79f0'),
        ),
    ]
