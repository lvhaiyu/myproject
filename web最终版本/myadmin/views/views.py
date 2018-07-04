from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Wordadmin
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
def index(request):

	return render(request,'myadmin/index.html')


# 后台登录
def login(request):
    
    # if request.method == 'GET':

    #     return render(request,'myadmin/login.html')

    # elif request.method == 'POST':

    #     # 执行登录

    #     return HttpResponse('执行登录')
	nexturl = request.GET.get('next','/')
	if request.method == "GET":
		return render(request,'myadmin/login.html')

	elif request.method == "POST":
		# 执行登录
		# 根据用户名先获取用户对象.在检测密码是否正确
		try:
			ob = Wordadmin.objects.get(username = request.POST['username'])
			# 检测密码是否正确
			res = check_password(request.POST['password'],ob.password)
			if res:
				# 密码正确
				request.session['AdminLogin'] = {'uid':ob.id,'username':ob.username}
				return HttpResponse('<script>alert("登录成功");location.href="/myadmin/"</script>')

		except:
			# 用户名错误
			pass
        
		return HttpResponse('<script>alert("用户名或密码错误");history.back(-1)</script>')

def logout(request):
	request.session['AdminLogin'] = {}
    
	return HttpResponse('<script>alert("退出成功");location.href="/myadmin/login/"</script>')