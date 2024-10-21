from rest_framework import generics
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer


class StudentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

# creating a new view for teachers


class TeacherListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
