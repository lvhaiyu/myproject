from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse

from .. models import Users
import os
# Create your views here.

def index(request):
    



    # 获取搜索条件
    types = request.GET.get('type',None)
    keywords = request.GET.get('keywords',None)

    # 判断是否具有搜索条件

    if types:
        # 有搜索条件
        if types == 'all':
            # 全条件搜索
            # select * from user where username like '%aa%' 
            from django.db.models import Q
            userlist = Users.objects.filter(
                Q(username__contains=keywords)|
                Q(age__contains=keywords)|
                Q(email__contains=keywords)|
                Q(phone__contains=keywords)|
                Q(sex__contains=keywords)
            )
        elif types == 'username':
            # 按照用户名搜索
            userlist = Users.objects.filter(username__contains=keywords)
        
        elif types == 'age':
            # 按照年龄搜索
            userlist = Users.objects.filter(age__contains=keywords)

        elif types == 'email':
            # 按照 email 搜索
            userlist = Users.objects.filter(email__contains=keywords)

        elif types == 'phone':
            # 按照 phone 搜索
            userlist = Users.objects.filter(phone__contains=keywords)

        elif types == 'sex':
            # 按照 sex 搜索
            userlist = Users.objects.filter(sex__contains=keywords)


    else:
        # 获取所有的用户数据
        userlist = Users.objects.filter()


    # 判断排序条件
    # userlist = userlist.order_by('-id')

    # 导入分页类
    from django.core.paginator import Paginator
    # 实例化分页对象,参数1,数据集合,参数2 每页显示条数
    paginator = Paginator(userlist, 10)
    # 获取当前页码数
    p = request.GET.get('p',1)
    # 获取当前页的数据
    ulist = paginator.page(p)

   
    # 分配数据
    context = {'userlist':ulist}
    
    # 加载模板
    return render(request,'myadmin/user/list.html',context)

def add(request):

	if request.method == "GET":

		return render(request,'myadmin/user/add.html')

	elif request.method =='POST':
		# data = {'carf'}
		try:
			data = request.POST.copy().dict()

			del data['csrfmiddlewaretoken']
			#mi ma jia mi  
			from django.contrib.auth.hashers import make_password, check_password
			data['password'] = make_password(data['password'],None,'pbkdf2_sha256')
			# 进行用户头像上传
			if request.FILES.get('pic',None):
				data['pic'] = uploads(request)
				if data['pic'] == 1:
					return HttpResponse('<script>alert("+++++");location.href="'+reverse('myadmin_user_add')+'"</script>')
			else:
				del data['pic']
			# print(request.POST)
			ob = Users.objects.create(**data)
			# print(ob)

			return HttpResponse('<script>alert("success");location.href="'+reverse('myadmin_user_list')+'"</script>'	)
		except:
			return HttpResponse('<script>alert("fiald");location.href="'+reverse('myadmin_user_add')+'"</script>'	)


def delete(request):
	try:

		uid = request.GET.get('uid',None)

		ob=Users.objects.get(id = uid)
		if ob.pic:
			os.remove('.'+ob.pic)
		ob.delete()
		data = {'msg':'sss','code':0}
	except:
		data = {'msg':'ffff','code':1}
	return JsonResponse(data)

def edit(request):
	
	uid = request.GET.get('uid',None)
	if not uid:
		return HttpResponse('<script>alert("没有用户数据");location.href="'+reverse('myadmin_user_list')+'"</script>')

	ob = Users.objects.get(id = uid )

	if request.method  == 'GET':

		context = {'uinfo':ob}

		return render(request,'myadmin/user/edit.html',context)
	
	elif request.method == 'POST':
		try:

			if request.FILES.get('pic',None):
			#
				if ob.pic:
				#
					os.remove('.'+ob.pic)
			#
				ob.pic = uploads(request)

			ob.username = request.POST['username']
			ob.email = request.POST['email']
			ob.age = request.POST['age']
			ob.sex = request.POST['sex']
			ob.phone = request.POST['phone']
			ob.save()
			return HttpResponse('<script>alert("success");location.href="'+reverse('myadmin_user_list')+'"</script>'	)
		except:
			return HttpResponse('<script>alert("fiald");location.href="'+reverse('myadmin_user_edit')+'"</script>'	)			


def uploads(request):
	myfile = request.FILES.get('pic',None)

	p = myfile.name.split('.').pop()
	arr = ['jpg','png','jpeg','gif']
	if p not in arr:
		return 1
	import time,random

	filename = str(time.time())+str(random.randint(1,99999))+'.'+p

	destination = open("./static/pics/"+filename,"wb+")

	for chunk in myfile.chunks():
		destination.write(chunk)

	destination.close()

	return '/static/pics/'+filename