from rest_framework import serializers
from studapp.models import Document
from studapp.models import Department
from studapp.models import Course_code
from studapp.models import Minor1
from studapp.models import Minor2
from studapp.models import Major
from studapp.models import Other

class DepartmentSerializer(serializers.ModelSerializer):
	course_code_set = serializers.StringRelatedField(many=True) #it has the coursecodes like apl100. This is the by default related name

	class Meta:
		model = Department
		fields = ('dept', 'code','course_code_set')

class Course_codeSerializer(serializers.ModelSerializer):
	minor1_set = serializers.StringRelatedField(many=True)
	minor2_set = serializers.StringRelatedField(many=True)
	major_set = serializers.StringRelatedField(many=True)
	other_set = serializers.StringRelatedField(many=True)

	class Meta:
		model = Course_code
		fields = ('code','pagehits','minor1_set','minor2_set','major_set','other_set')

class DocumentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Document
		fields = ('course_code','sem','year','type_exam','document','uploaded_at')


		