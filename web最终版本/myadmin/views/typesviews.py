from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
from .. models import Types
# Create your views here.
def gettypesorder():
	tlist = Types.objects.extra(select ={'paths':'concat(path,id)'}).order_by('paths')
	for x in tlist:
		if x.pid ==0:
			x.pname = '顶级分类'
		else:
			t = Types.objects.get(id=x.pid)
			x.pname = t.name
		num = x.path.count(',')-1
		x.name = (num*'|----')+x.name
	return tlist

def add(request):
	if request.method =='GET':
		tlist =gettypesorder()
		context = {'tlist':tlist}
		return render(request,'myadmin/types/add.html',context)
	elif request.method =='POST':
		ob=Types()
		ob.name = request.POST['name']
		ob.pid= request.POST['pid']
		if ob.pid =='0':
			ob.path='0,'
		else:
			t= Types.objects.get(id=ob.pid)
			ob.path =t.path+str(ob.pid)+','
		ob.save()
		return HttpResponse('<script>alert("添加成功");location.href="'+reverse('myadmin_types_list')+'"</script>')

def index(request):
	# tlist =gettypesorder()

	types = request.GET.get('type',None)
	keywords = request.GET.get('keywords',None)

	# 判断是否具有搜索条件

	if types:
	    # 有搜索条件
	    if types == 'all':
	        # 全条件搜索
	        # select * from user where username like '%aa%' 
	        from django.db.models import Q
	        typeslist = Types.objects.filter(
	           
	            Q(name__contains=keywords)

	            
	        )
	    
	    elif types == 'name':
	        # 按照年龄搜索
	        typeslist = Types.objects.filter(name__contains=keywords)


	else:
	    # 获取所有的用户数据
	    typeslist =gettypesorder()


	#判断排序条件
	# typeslist = typeslist.order_by('-id')
	
	
	# # 导入分页类
	from django.core.paginator import Paginator
	# 实例化分页对象,参数1,数据集合,参数2 每页显示条数
	paginator = Paginator(typeslist, 10)
	# 获取当前页码数
	p = request.GET.get('p',1)
	# 获取当前页的数据
	tlist = paginator.page(p)

	context ={'tlist':tlist}

	return render(request,'myadmin/types/list.html',context)

def delete(request):
	tid =request.GET.get('uid',None)

	num = Types.objects.filter(pid=tid).count()

	if num != 0:
		data ={'msg':'当前类下有子类,不能删除','code':1}
	else:
		ob=Types.objects.get(id=tid)
		ob.delete()
		data ={'msg':'删除成功','code':0}
	return JsonResponse(data)
def edit(request):

	uid = request.GET.get('uid',None)
	if not uid:
		return HttpResponse('<script>alert("没有用户数据");location.href="'+reverse('myadmin_types_list')+'"</script>')

	ob = Types.objects.get(id = uid )

	if request.method  == 'GET':

		context = {'uinfo':ob}

		return render(request,'myadmin/types/edit.html',context)
	
	elif request.method == 'POST':
		try:

			ob.name = request.POST['name']
			
			ob.save()
			return HttpResponse('<script>alert("success");location.href="'+reverse('myadmin_types_list')+'"</script>'	)
		except:
			return HttpResponse('<script>alert("fiald");location.href="'+reverse('myadmin_types_edit')+'"</script>'	)			
