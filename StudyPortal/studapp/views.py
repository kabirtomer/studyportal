# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *

def index(request):
	departments=Department.objects.order_by('dept')
	context={'departments':departments}
	return render(request,'studapp/index.html',context)
