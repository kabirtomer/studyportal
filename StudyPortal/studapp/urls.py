from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^view/$', views.display ,name='display'),
    
   # url(r'^upload/$', views.upload ,name='upload'),
	url(r'^upload/$', views.model_form_upload ,name='upload'),
	url(r'^thanks/$', views.thanks ,name='thanks'),
]
