from django.conf.urls import patterns,url

from images import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
    url(r'create/$',views.create, name='create'),
)
