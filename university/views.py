from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer


class StudentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

