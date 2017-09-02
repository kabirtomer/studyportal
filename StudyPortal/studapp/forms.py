from django import forms
from studapp.models import Document
from .models import *


class DocumentForm(forms.ModelForm):
	
	class Meta:
		model = Document
		fields = ('course_code','sem','year','type_exam', 'document')
		# course_code = models.ModelChoiceField(queryset=Course_code.objects.order_by('code'))
        


