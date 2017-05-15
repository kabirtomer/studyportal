from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^view/$', views.display ,name='display'),
    #url(r'^view?department=([0-9]+)&course_code=([0-9]+)/$',views.test,name='test'),
	
]
