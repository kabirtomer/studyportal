# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
###to change the filename of uploaded doc
import hashlib
import datetime
import os
from functools import partial

def _update_filename(instance, filename, path):
	path = path

	filename = instance.course_code+'_'+instance.year+'_sem'+instance.sem+'_'+instance.type_exam+'.pdf'

	return os.path.join(path, filename)

def upload_to(path):
	return partial(_update_filename, path=path)
# Create your models here.

#My plan is that we will have a table for DEPARTMENTS
#A table for COURSE CODE for each dept that will be linked to the department via Foreign keys
#tables for MINOR1, MINOR2, MAJOR, OTHER for each course code, again linked via foreign keys

class Department(models.Model):
	dept=models.CharField(max_length=50)
	def __str__(self):
		return self.dept

class Course_code(models.Model):
	dept=models.ForeignKey(Department,on_delete=models.CASCADE)
	code=models.CharField(max_length=6)#like APL100
	def __str__(self):
		return self.code

#For now, I'm not keeping a real file for the minor1 paper. Currently let's say I just place a string variable
class Minor1(models.Model):
	course=models.ForeignKey(Course_code,on_delete=models.CASCADE)
	#paper=models.CharField(max_length=50)
	paper = models.FileField()
	def __str__(self):
		return self.paper.name
	
class Minor2(models.Model):
	course=models.ForeignKey(Course_code,on_delete=models.CASCADE)
	#paper=models.CharField(max_length=50)
	paper = models.FileField()	
	def __str__(self):
		return self.paper.name
	
class Major(models.Model):
	course=models.ForeignKey(Course_code,on_delete=models.CASCADE)
	#paper=models.CharField(max_length=50)
	paper = models.FileField()
	def __str__(self):
		return self.paper.name
	
class Other(models.Model):
	course=models.ForeignKey(Course_code,on_delete=models.CASCADE)
	#paper=models.CharField(max_length=50)
	paper= models.FileField()
	def __str__(self):
		return self.paper.name
	
###uploaded unchecked document
class Document(models.Model):
	
	##########to get from the form
	course_code = models.CharField(max_length=6, blank=True,help_text="Eg. APL100")
	sem = models.CharField(max_length=20, blank=True,help_text="Eg. 1")
	year = models.CharField(max_length=20, blank=True,help_text="Eg. 2016-17")	
	type_exam = models.CharField(max_length=10, blank=True,help_text="Eg. minor1")
	document = models.FileField(upload_to=upload_to('documents/'))
	uploaded_at = models.DateTimeField(auto_now_add=True)
	##########
	def __str__(self):
		return self.course_code+'_'+self.year+'_sem'+self.sem+'_'+self.type_exam+'.pdf'

