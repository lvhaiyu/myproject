from django.conf.urls import url

from . views import views,userviews,typesviews,goodsviews

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
	# url(r'^types/edit/$', typesviews.edit,name='myadmin_types_edit'),
    #
    url(r'^goods/add/$', goodsviews.add,name='myadmin_goods_add'),
    url(r'^goods/index/$', goodsviews.index,name='myadmin_goods_list'),
    # url(r'^goods/delete/$', goodsviews.delete,name='myadmin_goods_delete'),
    # url(r'^goods/edit/$', goodsviews.edit,name='myadmin_goods_edit'),   
    ]