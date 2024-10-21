from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .models import Student, Course, Takes
from .serializers import StudentSerializer, CourseSerializer, TakesSerializer
from .filter_backends import StudentFilter


class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()


class TeacherListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = StudentFilter
    search_fields = ['name', 'last_name']
    ordering_fields = ['student_id', 'name', 'birth_date']


class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TakesViewSet(ModelViewSet):
    queryset = Takes.objects.all()
    serializer_class = TakesSerializer