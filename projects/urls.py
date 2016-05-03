from django.conf.urls import patterns,url

from projects import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
    url(r'[0-9a-f]{32}',views.show,name='show'),
    url(r'create$',views.create, name='create'),
    url(r'delete/$',views.delete,name='delete'),
    url(r'update/',views.update,name='update'),
)
