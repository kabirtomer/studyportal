# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import *

from django.forms import ModelForm
from study.forms import *
from study.models import Document
import os
from django.core.files import File

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

#import for apis
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

def track_hits(request,template_path,context,co):
        try:
                co.pagehits+=1
        except:
                co.pagehits = 1
        co.save()
        return render(request,template_path,context)

def index(request):
	departments=Department.objects.order_by('dept')
	courses=Course_code.objects.order_by('code')
	context={'departments':departments,'courses':courses}

	return render(request,'study/index.html',context)

def indexl(request):
	departments=Department.objects.order_by('dept')
	courses=Course_code.objects.order_by('code')
	context={'departments':departments,'courses':courses}
	return render(request,'study/indexl.html',context)

def display(request):
	all_departments=Department.objects.order_by('dept')
	all_courses=Course_code.objects.order_by('code')
	department_id=request.GET.get('department','None')
	#course_code_id=request.GET.get('course_code','None')
	try:
		course_code_id=Course_code.objects.get(code=request.GET.get('course_code','None').upper()).id
	except:
		course_code_id='0'
	if department_id=='0' and course_code_id=='0':
		return render(request,'study/index.html',{'departments':all_departments,'courses':all_courses})
	elif course_code_id=='0':
		dept=Department.objects.get(pk=department_id)
		return render(request,'study/get_course_codes.html',{'department':dept,'departments':all_departments,'courses':all_courses})

	else:
		course=Course_code.objects.get(pk=course_code_id)
		return track_hits(request,'study/get_papers.html',{'course':course,'departments':all_departments,'courses':all_courses},course)

def displayl(request):
	all_departments=Department.objects.order_by('dept')
	all_courses=Course_code.objects.order_by('code')
	department_id=request.GET.get('department','None')
	#course_code_id=request.GET.get('course_code','None')
	try:
		course_code_id=Course_code.objects.get(code=request.GET.get('course_code','None').upper()).id
	except:
		course_code_id='0'
	if department_id=='0' and course_code_id=='0':
		return render(request,'study/indexl.html',{'departments':all_departments,'courses':all_courses})
	elif course_code_id=='0':
		dept=Department.objects.get(pk=department_id)
		return render(request,'study/get_course_codesl.html',{'department':dept,'departments':all_departments,'courses':all_courses})
	else:
		course=Course_code.objects.get(pk=course_code_id)
		return track_hits(request,'study/get_papersl.html',{'course':course,'departments':all_departments,'courses':all_courses},course)

# def upload(request):
#         departments=Department.objects.order_by('dept')
# 	courses=Course_code.objects.order_by('code')
# 	context={'departments':departments,'courses':courses}
#         return render(request,'study/upload.html', context)

# def uploadl(request):
#         departments=Department.objects.order_by('dept')
# 	courses=Course_code.objects.order_by('code')
# 	context={'departments':departments,'courses':courses}
#         return render(request,'study/uploadl.html', context)

####upload file
def thanks(request):
	return render(request,'study/thanks.html')
def thanksl(request):
	return render(request,'study/thanksl.html')

# def model_form_upload(request):
# 	if request.method == 'POST':
# 		form = DocumentForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			# return redirect('thanks')
# 			txtfile = open('media/unapproved_documents/files.txt','a')
# 			txtfile.write(request.POST.get('course_code','none')+'_'+request.POST.get('year','none')+'_sem'+request.POST.get('sem','none')+'_'+request.POST.get('type_exam','none')+request.FILES['document'].name[request.FILES['document'].name.rindex('.'):]+'\n')
			
# 			txtfile.close()

# 			return render(request,'study/thanks.html')

# 	else:
# 		form = DocumentForm()
# 	return render(request, 'study/model_form_upload.html', {'form': form})
def model_form_upload(request):
	if request.method == 'POST':

		doc = Document(course_code = request.POST.get('course_code'),sem = request.POST.get('sem'),year = request.POST.get('year'),type_exam = request.POST.get('type_exam'))
		doc.document = request.FILES['document']
		doc.save()

		txtfile = open('media/unapproved_documents/files.txt','a')
		txtfile.write(request.POST.get('course_code','none')+'_'+request.POST.get('year','none')+'_sem'+request.POST.get('sem','none')+'_'+request.POST.get('type_exam','none')+request.FILES['document'].name[request.FILES['document'].name.rindex('.'):]+'\n')
		
		txtfile.close()
		return render(request,'study/thanks.html')

	else:
		return render(request, 'study/model_form_upload.html')


def model_form_uploadl(request):
	if request.method == 'POST':
		
		doc = Document(course_code = request.POST.get('course_code'),sem = request.POST.get('sem'),year = request.POST.get('year'),type_exam = request.POST.get('type_exam'))
		doc.document = request.FILES['document']
		doc.save()

		txtfile = open('media/unapproved_documents/files.txt','a')
		txtfile.write(request.POST.get('course_code','none')+'_'+request.POST.get('year','none')+'_sem'+request.POST.get('sem','none')+'_'+request.POST.get('type_exam','none')+request.FILES['document'].name[request.FILES['document'].name.rindex('.'):]+'\n')
		
		txtfile.close()
		return render(request,'study/thanksl.html')

	else:
		return render(request, 'study/model_form_uploadl.html')
#approvals
@login_required
def approve(request):
	txtfile = open('media/unapproved_documents/files.txt','r')
	unapproved_documents = txtfile.readlines()
	txtfile.close
	return render(request, 'study/approve.html', {'unapproved_documents':unapproved_documents})

@login_required
def remove_unapproved_document(request):
	Document.objects.all().delete()#to remove model objects of unnecessary document model
	txtfile = open('media/unapproved_documents/files.txt','r')
	lines = txtfile.readlines()
	txtfile.close()
	txtfile = open('media/unapproved_documents/files.txt','w')
	for line in lines:
		if line != request.GET.get('name','none')+"\n":
			txtfile.write(line)
	txtfile.close()
	try:
		os.remove('media/unapproved_documents/'+request.GET.get('name','none'))
	except:
		return HttpResponse('<h1>No such file exists. Maybe it was manually deleted</h1>')
	return redirect('/study/approve')

#login to approve
@login_required
def approve_unapproved_document(request):
	fileName = request.GET.get('name','none')
	try:
		if fileName[fileName.rindex('_')+1:fileName.rindex('.')].upper() == "MAJOR":
			coursecode = Course_code.objects.get(code=fileName[0:6].upper())
			newpaper = Major(course = coursecode)
			newpaper.paper.save(fileName, File(open("media/unapproved_documents/"+fileName)))
			newpaper.save()
			return redirect('/study/remove_unapproved_document?name='+fileName)
		elif fileName[fileName.rindex('_')+1:fileName.rindex('.')].upper() == "MINOR1":
			coursecode = Course_code.objects.get(code=fileName[0:6].upper())
			newpaper = Minor1(course = coursecode)
			newpaper.paper.save(fileName, File(open("media/unapproved_documents/"+fileName)))
			newpaper.save()
			return redirect('/study/remove_unapproved_document?name='+fileName)
		elif fileName[fileName.rindex('_')+1:fileName.rindex('.')].upper() == "MINOR2":
			coursecode = Course_code.objects.get(code=fileName[0:6].upper())
			newpaper = Minor2(course = coursecode)
			newpaper.paper.save(fileName, File(open("media/unapproved_documents/"+fileName)))
			newpaper.save()
			return redirect('/study/remove_unapproved_document?name='+fileName)
		else :
			coursecode = Course_code.objects.get(code=fileName[0:6].upper())
			newpaper = Other(course = coursecode)
			newpaper.paper.save(fileName, File(open("media/unapproved_documents/"+fileName)))
			newpaper.save()
			return redirect('/study/remove_unapproved_document?name='+fileName)
	except:
		return HttpResponse('<h1> Such a course code does not exist</h1><h1>Ask the developers to add the course code and then try again</h1>')
	
def userlogin(request):
	if request.method=='POST':
		user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
		if user is not None:
			login(request,user)
			return redirect('/study/approve')

		else:
			render(request,'study/login.html')
	return render(request,'study/login.html')
def userlogout(request):
	logout(request)
	# return render(request,'study/login.html')
	return redirect("/study/light/")
#api

class DepartmentList(APIView):
	def get(self, request):
		# departments = Department.objects.all()
		# serializer  = DepartmentSerializer(departments, many = True)
		# return Response(serializer.data)

		tmp = request.GET.get('code','None').upper()
		if tmp!='NONE':
			try:
				department=Department.objects.get(code=tmp)
				serializer  = DepartmentSerializer(department, many = False)
				return Response(serializer.data)
			except:
				# serializer  = Course_codeSerializer( many = False)
				return Response(status=status.HTTP_400_BAD_REQUEST)	
		else:
			departments=Department.objects.all()
			serializer  = DepartmentSerializer(departments, many = True)
			return Response(serializer.data)

	
class Course_codeList(APIView):
	def get(self, request):
		# course_codes = Course_code.objects.all()
		tmp = request.GET.get('code','None').upper()
		if tmp!='NONE':
			try:
				course=Course_code.objects.get(code=tmp)
				serializer  = Course_codeSerializer(course, many = False)
				return Response(serializer.data)
			except:
				# serializer  = Course_codeSerializer( many = False)
				return Response(status=status.HTTP_400_BAD_REQUEST)	
		else:
			courses=Course_code.objects.all()
			serializer  = Course_codeSerializer(courses, many = True)
			return Response(serializer.data)


		
class DocumentList(APIView):
	# def get(self, request):
	# 	documents=Document.objects.all()
	# 	serializer  = DocumentSerializer(documents, many = True)
	# 	return Response(serializer.data)


	def post(self, request):
		serializer = DocumentSerializer(data = request.data)
		


		if serializer.is_valid() and request.data.get('course_code')!=None and request.data.get('type_exam')!=None: 
			txtfile = open('media/unapproved_documents/files.txt','a')
			txtfile.write(request.POST.get('course_code','none')+'_'+request.POST.get('year','')+'_sem'+request.POST.get('sem','')+'_'+request.POST.get('type_exam','none')+request.FILES['document'].name[request.FILES['document'].name.rindex('.'):]+'\n')
			txtfile.close()
			serializer.save() 
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
