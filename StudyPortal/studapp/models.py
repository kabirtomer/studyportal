# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
	paper=models.CharField(max_length=50)
	def __str__(self):
		return self.paper
	
class Minor2(models.Model):
	course=models.ForeignKey(Course_code,on_delete=models.CASCADE)
	paper=models.CharField(max_length=50)
	def __str__(self):
		return self.paper
	
class Major(models.Model):
	course=models.ForeignKey(Course_code,on_delete=models.CASCADE)
	paper=models.CharField(max_length=50)
	def __str__(self):
		return self.paper
	
class Other(models.Model):
	course=models.ForeignKey(Course_code,on_delete=models.CASCADE)
	paper=models.CharField(max_length=50)
	def __str__(self):
		return self.paper
	
