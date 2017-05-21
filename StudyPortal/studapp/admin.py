# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Department)
admin.site.register(Course_code)
admin.site.register(Minor1)
admin.site.register(Minor2)
admin.site.register(Major)
admin.site.register(Other)
admin.site.register(Document)
