# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import *

from django.forms import ModelForm
from studapp.forms import *
from studapp.models import Document

def indexl(request):
	departments=Department.objects.order_by('dept')
	courses=Course_code.objects.order_by('code')
	context={'departments':departments,'courses':courses}
	return render(request,'studapp/indexl.html',context)

#test is just a debug function
def test(request,x,y):
	departments=Department.objects.order_by('dept')
	courses=Course_code.objects.order_by('code')
	context={'departments':departments,'courses':courses,'x':x,'y':y}
	return render(request,'studapp/index_old.html',context)

def displayl(request):
	all_departments=Department.objects.order_by('dept')
	all_courses=Course_code.objects.order_by('code')
	department_id=request.GET.get('department','None')
	#course_code_id=request.GET.get('course_code','None')
	try:
		course_code_id=Course_code.objects.get(code=request.GET.get('course_code','None')).id
	except:
		course_code_id='0'
	if department_id=='0' and course_code_id=='0':
		return render(request,'studapp/indexl.html',{'departments':all_departments,'courses':all_courses})
	elif course_code_id=='0':
		dept=Department.objects.get(pk=department_id)
		return render(request,'studapp/get_course_codesl.html',{'department':dept,'departments':all_departments,'courses':all_courses})

	else:
		course=Course_code.objects.get(pk=course_code_id)
		return render(request,'studapp/get_papersl.html',{'course':course,'departments':all_departments,'courses':all_courses})

def uploadl(request):
        departments=Department.objects.order_by('dept')
	courses=Course_code.objects.order_by('code')
	context={'departments':departments,'courses':courses}
        return render(request,'studapp/uploadl.html', context)

####upload file
def thanksl(request):
	return render(request,'studapp/thanksl.html')
def model_form_uploadl(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('thanks')
	else:
		form = DocumentForm()
	return render(request, 'studapp/model_form_uploadl.html', {'form': form})
