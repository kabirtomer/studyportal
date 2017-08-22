from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^light/$', views.indexl, name='indexl'),
    url(r'^view/$', views.display ,name='display'),
    url(r'^light/view/$', views.displayl ,name='displayl'),
    
   # url(r'^upload/$', views.upload ,name='upload'),
    url(r'^upload/$', views.model_form_upload ,name='upload'),
    url(r'^light/upload/$', views.model_form_uploadl ,name='uploadl'),
    url(r'^light/thanks/$', views.thanksl ,name='thanksl'),
    url(r'^thanks/$', views.thanks ,name='thanks'),
    url(r'^rest/(?P<pk>[0-9A-Z]+)/$', views.restCheck),
]
