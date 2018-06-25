from django.conf.urls import url

from . views import views,userviews

urlpatterns = [
  
    url(r'^$',views.index,name='myadmin_index'),
    
    url(r'^user/add/$',userviews.add,name='myadmin_user_add'),
    url(r'^user/index/$',userviews.index,name='myadmin_user_list'),
    url(r'^user/delete/$',userviews.delete,name='myadmin_user_delete'),
    url(r'^user/edit/$',userviews.edit,name='myadmin_user_edit'),
   


]