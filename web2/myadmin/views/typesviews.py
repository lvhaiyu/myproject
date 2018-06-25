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
			x.panme = t.name
		num = x.path.count(',')-1
		x.name = (num*'|----')+x.name
	return tlist

def add(request):
	if request.method =='GET':
		tlist =gettypesorder()
		context = {'tlist':tlist}
		return render(rquest,'myadmin/types/add.html',context)
	elif request.method =='POST':
		ob.Types()
		ob.name = request.POST['name']
		ob.pid= request.POST['oid']
		if ob.pid =='0':
			ob.path='0,'
		else:
			t= Types.objects.get(id=ob.pid)
			ob.path =t.path+str(ob.pid)+','
		ob.save()
		return HttpResponse('<script>alert("添加成功");location.href="'+reverse('myadmin_types_list')+'"</script>')

def index(request):
	tlist =gettypesorder()
	context ={'tlist':tlist}

	return render(request,'myadmin/types/list.html',context)

def delete(request):
	tid =request.GET.get('uid',None)

	num = Types.objects.filter(pid=tid).count()

	if num != 0:
		data ={'msg':'当前类下有子类,不能删除','code':1}
	else:
		ob.Types.objects.get(id=tid)
		ob.delete()
		data ={'msg':'删除成功','code':0}
	return JsonResponse(data)
	def edit(request):

		pass