#coding=utf-8
from django.contrib import admin
from models import *
from df_user import views

# Register your models here.
class GoodsInline(admin.TabularInline):
    model = GoodsInfo
    extra = 1



class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle','isDelete']
    search_fields = ['ttitle']
    list_filter = ['ttitle']
    # inlines = [
    #     GoodsInline
    # ]
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'ttitle')

class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','gtitle','classify','gpic','gprice','gstocks',
                    'Gunit','gclick','gbrief',
                    'Gadv','IsDelete']
    search_fields = ['gtitle','gprice']
    # date_hierarchy = 'go_time'  # 详细时间分层筛选　
    list_filter = ['gtitle']
    fieldsets = (
        ('None',{'fields':['gtitle',('gpic','classify'),('gprice','gstocks')]}),
        (u'商品详情',{
            'classes':('collapse',),
            'fields':['gunit','gclick','gbrief','gcontent']}),
        (u'分类', {
            'classes': ('collapse',),
            'fields': ['gadv','isDelete']}),
    )
    fk_fields=('classify',)

    # ordering设置默认排序字段，负号表示降序排序
    # ordering = ('-name',)
    # 操作项功能显示选中项的数目
    actions_selection_counter = True
    # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # list_editable 设置默认可编辑字段（gtitle默认不可编辑，因为它是一个链接，点击会进入修改页面）
    # list_editable = ['gtitle', 'gprice']
    #list_editable = ['gprice','classify']

    # def get_queryset(self, request):
    #     """函数作用：使当前登录的用户只能看到自己负责的服务器"""
    #     qs = super(GoodsInfoAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=UserInfo.objects.filter(user_name=request.uname))



admin.site.site_header = '鲜稻屋台管理'
admin.site.site_title = '鲜稻屋'

admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)