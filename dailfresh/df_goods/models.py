#coding=utf-8
from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField
from django.utils.html import format_html

from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
class TypeInfo(models.Model):
    ttitle=models.CharField('分类名称',max_length=20)
    isDelete=models.BooleanField('是否删除',default=False)
    def __str__(self):
        return self.ttitle.encode('utf-8')
    class Meta:
        verbose_name = '商品分类'  #指定在admin管理界面中显示的名称
        verbose_name_plural = '商品分类'  #指定在admin管理界面中显示的名称

# @python_2_unicode_compatible
class GoodsInfo(models.Model):
    gtitle=models.CharField('商品名称',max_length=20)
    gpic=models.ImageField('图片',upload_to='df_goods')
    gprice=models.DecimalField('价格',max_digits=9,decimal_places=2)
    gunit=models.CharField('单位',max_length=20,default='500g')
    gclick=models.IntegerField('点击量',)
    gbrief=models.CharField('简介',max_length=200)
    gstocks=models.IntegerField('库存量',)
    gcontent=HTMLField('详细简绍',)
    gadv=models.BooleanField('广告',default=False)
    classify=models.ForeignKey(TypeInfo)
    isDelete=models.BooleanField('是否删除',default=False)
    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'
    def __str__(self):
        return self.gtitle.encode('utf-8')

    def Gadv(self):   #需要在admin中替换gadv
        if self.gadv:
            color_code = 'red'
            state='是'
            # return '是'
        else:
            color_code = 'green'
            state = '否'
            # return '否'
        return format_html(
            '<span style="color:{};">{}</span>',
            color_code,
            state,
        )

    Gadv.short_description = '广告'

    def Gunit(self):   #需要在admin中替换gadv
        if self.gunit== '500g' :
            color_code = 'red'
        else:
            color_code = 'green'
        return format_html(
            '<span style="color:{};">{}</span>',
            color_code,
            self.gunit,
        )

    Gunit.short_description = '单位'



    def IsDelete(self):   #需要在admin中替换gadv
        if self.isDelete:
            return '是'
        else:
            return '否'
    IsDelete.short_description = '是否删除'

    # def Gtype(self):
    #     return format_html(self.gtype)
    # Gtype.admin_order_field = 'gtype'
    # Gtype.short_description = '种类'

    # def Gtitle(self):
    #     return self.gtitle
    # Gtitle.short_description = '商品名称'
    # IsDelete.short_description='是否删除'
    # Gprice.short_description = '价格'
    # gpic.short_description = '图片'

