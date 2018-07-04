from django.conf.urls import url

from . views import views,userviews,typesviews,goodsviews,backviews

urlpatterns = [
  
    url(r'^$',views.index,name='myadmin_index'),
    #
    url(r'^user/add/$',userviews.add,name='myadmin_user_add'),
    url(r'^user/index/$',userviews.index,name='myadmin_user_list'),
    url(r'^user/delete/$',userviews.delete,name='myadmin_user_delete'),
    url(r'^user/edit/$',userviews.edit,name='myadmin_user_edit'),
   

    # 商品分类管理
	url(r'^types/add/$', typesviews.add,name='myadmin_types_add'),
	url(r'^types/index/$', typesviews.index,name='myadmin_types_list'),
	url(r'^types/delete/$', typesviews.delete,name='myadmin_types_delete'),
	url(r'^types/edit/$', typesviews.edit,name='myadmin_types_edit'),
    #
    url(r'^goods/add/$', goodsviews.add,name='myadmin_goods_add'),
    url(r'^goods/index/$', goodsviews.index,name='myadmin_goods_list'),
    url(r'^goods/delete/$', goodsviews.delete,name='myadmin_goods_delete'),
    url(r'^goods/edit/$', goodsviews.edit,name='myadmin_goods_edit'), 
    #  
    # url(r'^orders/list/$', orderviews.list,name='myadmin_orders_list'),
    # url(r'^orders/edit/$', orderviews.edit,name='myadmin_orders_edit'),
	# 后台订单列表
    url(r'^back/list/$', backviews.list,name='myadmin_back_list'),

    url(r'^back/edit/$',backviews.edit,name='myadmin_back_edit'),

    url(r'^back/info/$',backviews.info,name='myadmin_back_info'),

    # 后台登录和登录验证....
    url(r'^login/$', views.login,name='myadmin_login'),
	# 后台退出
	url(r'^logout/$', views.logout,name='myadmin_logout'),


    ]