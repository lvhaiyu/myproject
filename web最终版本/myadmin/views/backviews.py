from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse

from .. models import Users,Types,Goods,Address,Orders,OrderInfo
import os

# Create your views here.
# 订单列表
def list(request):
    #获取搜索条件
    types = request.GET.get('type',None)
    keywords = request.GET.get('keywords',None)

    #判断是否具有搜索条件

    if types:
    #有搜索条件
        if types == 'all':
            try:
                keywords1 = Address.objects.get(name=keywords).id
                #全条件搜索
                #select * from user where username like '%aa%' 
                from django.db.models import Q
                userlist = Orders.objects.filter(
                    Q(addressid=keywords1)|
                    Q(totalprice__contains=keywords)|
                    Q(totalnum__contains=keywords)
                )
            except:
                from django.db.models import Q
                userlist = Orders.objects.filter(
                    Q(totalprice__contains=keywords)|
                    Q(totalnum__contains=keywords)
                )

        elif types == 'totalprice':
            # 按照title搜索
            userlist = Orders.objects.filter(totalprice__contains=keywords)

        elif types == 'totalnum':
            userlist = Orders.objects.filter(totalnum__contains=keywords)

        elif types == 'sname':
            keywords1 = Address.objects.get(name=keywords).id
            userlist = Orders.objects.filter(addressid=keywords1)

        elif types == 'saddress':
            keywords2 = Address.objects.get(address=keywords).id
            userlist = Orders.objects.filter(addressid=keywords2)
    else:
        # 获取所有的用户数据
        userlist = Orders.objects.filter()

    # 获取所有的用户数据
    # userlist = Goods.objects.all()

    #导入分页类
    from django.core.paginator import Paginator

    # 实例化分页对象,参数1,数据集合,参数2 每页显示条数
    paginator = Paginator(userlist, 5)

    #获取当前页码数
    p = request.GET.get('p',1)

    #获取当前页的数据
    dlist = paginator.page(p)


    context = {'userlist':dlist}

    return render(request,'myadmin/back/list.html',context)

def edit(request):
    # 接受参数
    uid = request.GET.get('uid',None)
    # 获取对象
    ob = Orders.objects.get(id=uid)

    if request.method == 'GET':

        # 分配数据
        context = {'uinfo':ob}
        # 显示编辑页面
        return render(request,'myadmin/back/edit.html',context)

    elif request.method == 'POST':
        try:            
            ob.status = request.POST['status']
            ob.save()

            return HttpResponse('<script>alert("更新成功");location.href="'+reverse('myadmin_back_list')+'"</script>')
        except:
            return HttpResponse('<script>alert("更新失败");location.href="'+reverse('myadmin_edit')+'?uid='+str(ob.id)+'"</script>')

def info(request):
    #接受参数
    uid = request.GET.get('uid',None)
    #获取订单的详情
    dlist = Orders.objects.get(id=uid)

    dlist = dlist.orderinfo_set.all()
    
    # errdata = []
    # for i in dlist:
    #   i.goodssub = Orders.objects.filter(gid=i.id)
    #   errdata.append(i)

    # print(errdata.title)

    context = {'userlist':dlist}

    return render(request,'myadmin/back/info.html',context)
    # return HttpResponse('1')