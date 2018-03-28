# coding=utf-8
from haystack import indexes
from models import GoodsInfo


class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return GoodsInfo  #写数据表名字

    def index_queryset(self, using=None):
        return self.get_model().objects.all() #对数据表中的那些数据进行解锁
