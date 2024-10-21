<<<<<<< HEAD
from rest_framework import generics
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer
=======
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Student
from .serializers import StudentSerializer
from .filter_backends import StudentFilter
>>>>>>> 34e4c16ab687084899aee374dbf5cf5a5b1a2e3b


class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
<<<<<<< HEAD

# creating a new view for teachers


class TeacherListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
=======
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = StudentFilter
    search_fields = ['name', 'last_name'] 
    ordering_fields = ['student_id', 'name', 'birth_date']
>>>>>>> 34e4c16ab687084899aee374dbf5cf5a5b1a2e3b
