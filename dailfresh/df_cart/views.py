#coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from df_user import user_decorator
from django.http import HttpResponseRedirect ,JsonResponse ,HttpResponse
from models import *
from django.shortcuts import redirect
# Create your views here.

@user_decorator.login
def cart(request):
    uid = request.session['user_id']
    casts= CartInfo.objects.filter(user_id=uid)
    casts_conut=casts.count()
    context={
        'title':'购物车',
        'carts':casts,
        'page_name': 1,
        'casts_conut':casts_conut,
    }
    return render(request,'df_cart/cart.html',context)


@user_decorator.login
def add(request,gid,count):
    #用户uid购买了gid商品，数量为count
    uid=request.session['user_id']
    gid1=int(gid)
    count=int(count)
    #查询购物车中是否已经有此商品，如果有则数据量加，如果没有则新增
    carts=CartInfo.objects.filter(user_id=uid,goods_id=gid)
    if len(carts)>=1 :
        cart=carts[0]
        cart.count=cart.count+count
    else:
        cart=CartInfo()
        cart.user_id=uid
        cart.goods_id=gid1
        cart.count=count
    cart.save()
    #如果是ajax请求则返回json,否则转向购物车
    if request.is_ajax():
        count=CartInfo.objects.filter(user_id=request.session['user_id']).count()
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/')

def carts_count(request):
    print('nimeiya')
    count=CartInfo.objects.filter(user_id=request.session['user_id']).count()
    return JsonResponse({'count': count})






















