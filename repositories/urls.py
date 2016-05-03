from django.conf.urls import patterns,url

from repositories import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
    url(r'^\d+$',views.show, name='detail'),
    url(r'create/$',views.create, name='create'),
    url(r'delete/$',views.delete,name='delete'),
    url(r'update/',views.update,name='update'),
    url(r'list/',views.list,name='list'),
)
