#coding=utf-8
from django.shortcuts import render,redirect
from django.http import *
from hashlib import sha1
from models import *
# Create your views here.
def register(request):
    return render(request,'df_user/register.html',{'title':"注册"})

def register_handle(request):
    #接收用户输入
    post=request.POST
    uname=post.get('user_name')
    upwd = post['pwd']
    ucpwd = post['cpwd']
    uemail = post['email']
    #判断两次密码输入是否一致
    if ucpwd!=upwd:
        return redirect('/user/register/')
    #密码加密
    sha1pwd=sha1()
    sha1pwd.update(upwd)
    upwd2=sha1pwd.hexdigest()

    #创建对象
    user=UserInfo()
    user.uname=uname
    user.upwd = upwd2
    user.uemail=uemail
    user.save()
    #注册成功转到登录页面
    return redirect('/user/login/')

def register_exist(request):
    uname = request.GET.get('uname')
    count=UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def login(request):
    uname=request.COOKIES.get('uname','')
    context={'title':'用户登录','error_name': 0,'error_pwd': 0,'uname':uname}
    return render(request,'df_user/login.html',context)

def login_handle(request):
    #接收请求信息
    post=request.POST
    uname=post.get('username')
    upwd=post.get('pwd')
    rember=post.get('rember',0)
    #根据用户名查询对象
    user=UserInfo.objects.filter(uname=uname) #[]
    print(user)
    print uname
    #判断：如果未查找到用户名错，如果查到，判断密码是否正确，正确则转到用户中心
    if len(user)==1 :
        s1=sha1()
        s1.update(upwd)
        if s1.hexdigest()==user[0].upwd :
            red=HttpResponseRedirect('/user/info/')
            #记住用户名
            if rember!=0 :
                red.set_cookie('uname',uname)
            else :
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id']=user[0].id
            request.session['user_name']=uname
            print('ok1')
            return  red
        else :
            context = {'title':'用户登录','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
            print('error_mima1')
            return render(request,'df_user/login.html',context)
    else :
        context = {'title':'用户登录','error_name':1,'error_pwd':0,'uname':uname,'upwd':upwd}
        print('error_usemane')
        return render(request, 'df_user/login.html', context)


def info(request):
    user_email=UserInfo.objects.get(id=request.session['user_id']).uemail
    context={'title':'用户中心','user_email':user_email,'user_name':request.session['user_name']}
    return  render(request,'df_user/user_center_info.html',context)

def site(request):
    user=UserInfo.objects.get(id=request.session['user_id'])
    if request.method=='POST':
        post=request.POST
        user.ushou=post['ushou']
        user.uaddress=post['uaddress']
        user.uyoubian=post['uyoubian']
        user.uphone=post['uphone']
        user.save()
    context={'title':'用户中心','user':user}
    return render(request,'df_user/user_center_site.html',context)




































