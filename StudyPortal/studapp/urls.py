from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.indexl, name='index'),
    url(r'^view/$', views.displayl ,name='display'),
    
   # url(r'^upload/$', views.upload ,name='upload'),
	url(r'^upload/$', views.model_form_uploadl ,name='upload'),
	url(r'^thanks/$', views.thanksl ,name='thanks'),
]
