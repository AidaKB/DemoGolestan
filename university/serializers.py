from rest_framework import serializers
from .models import Student, Course, Takes, Teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    # taking a list from teachers

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class ListTakesSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = Takes
        fields = '__all__'


class CreateTakesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Takes
        fields = '__all__'


