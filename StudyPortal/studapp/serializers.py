from studapp.models import *
from rest_framework import serializers

class StudySerializer(serializers.Serializer):
    coursecode = serializers.CharField(required=True, max_length=6)
    # paper = serializers.FileField()
    other_papers = serializers.CharField(max_length=200)
    
    def create(self, validated_data):
        return Listfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.coursecode = validated_data.get('coursecode', instance.course)
        # instance.paper = validated_data.get('paper', instance.paper)
        course_id = Course_Code.objects.get(code=coursecode).id
        others = Other.objects.get(course=course_id)
        other_papers = ''
        for o in others:
            other_papers = other_papers+o.paper.name+', '
        instance.other_papers = other_papers
        instance.save()
        return instance

    '''class Meta:
        model = Listfile
        fields = ('coursecode',)'''
