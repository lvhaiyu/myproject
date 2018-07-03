from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .. models import OrderInfo,Orders

# Create your views here.
def list(request):

	orders=Orders.objects.all()
	context = {'orders':orders}

	# 加载模板
	return render(request,'myadmin/orders/list.html',context)
def edit(request):

	pass