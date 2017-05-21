from django import forms
from studapp.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('course_code','sem','year','type_exam', 'document', )
