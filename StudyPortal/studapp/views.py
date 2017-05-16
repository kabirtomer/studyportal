# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *

def index(request):
	departments=Department.objects.order_by('dept')
	courses=Course_code.objects.order_by('code')
	context={'departments':departments,'courses':courses}
	return render(request,'studapp/index.html',context)

#test is just a debug function
def test(request,x,y):
	departments=Department.objects.order_by('dept')
	courses=Course_code.objects.order_by('code')
	context={'departments':departments,'courses':courses,'x':x,'y':y}
	return render(request,'studapp/index_old.html',context)

def display(request):
	all_departments=Department.objects.order_by('dept')
	all_courses=Course_code.objects.order_by('code')
	department_id=request.GET.get('department','None')
	course_code_id=request.GET.get('course_code','None')
	
	if department_id=='0' and course_code_id=='0':
		return render(request,'studapp/index.html',{'departments':all_departments,'courses':all_courses})
	elif course_code_id=='0':
		dept=Department.objects.get(pk=department_id)
		return render(request,'studapp/get_course_codes.html',{'department':dept,'departments':all_departments,'courses':all_courses})

	else:
		course=Course_code.objects.get(pk=course_code_id)
		return render(request,'studapp/get_papers.html',{'course':course,'departments':all_departments,'courses':all_courses})

def upload(request):
        departments=Department.objects.order_by('dept')
	courses=Course_code.objects.order_by('code')
	context={'departments':departments,'courses':courses}
        return render(request,'studapp/upload.html', context)
