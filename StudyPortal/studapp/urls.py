from django.conf.urls import url

from . import views

from rest_framework.urlpatterns import format_suffix_patterns

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
    url(r'^userlogin/$', views.userlogin ,name='userlogin'),
    url(r'^userlogout/$', views.userlogout ,name='userlogout'),

    url(r'^api/departments/$', views.DepartmentList.as_view() ),
    url(r'^api/course_codes/$', views.Course_codeList.as_view() ),
    url(r'^api/document/$', views.DocumentList.as_view() ),






]

urlpatterns = format_suffix_patterns(urlpatterns)
