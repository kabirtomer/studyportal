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

	url(r'^approve/$', views.approve ,name='approve'),
    url(r'^remove_unapproved_document/$', views.remove_unapproved_document ,name='remove_unapproved_document'),
    url(r'^approve_unapproved_document/$', views.approve_unapproved_document ,name='approve_unapproved_document'),


]
