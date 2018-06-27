from django.conf.urls import url

from . import views 

urlpatterns = [
    # 首页 
    url(r'^$', views.index,name='myhome_index'),
    # 列表
    url(r'^list/(?P<tid>[0-9]+)/$', views.list,name='myhome_list'),
    # 搜索
    url(r'^search/$', views.search,name='myhome_search'),
    # 详情
    url(r'^info/(?P<sid>[0-9]+)/$', views.info,name='myhome_info'),
    # 登录
    url(r'^login/$', views.login,name='myhome_login'),
    # 退出登录
    url(r'^logout/$', views.logout,name='myhome_logout'),
    # 注册
    url(r'^register/$', views.register,name='myhome_register'),
    # 验证码
    url(r'^vcode/$', views.vcode,name='myhome_vcode'),



    # 购物车

    # 订单

    # 个人中心
]