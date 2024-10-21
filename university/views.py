from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Student
from .serializers import StudentSerializer
from .filter_backends import StudentFilter


class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = StudentFilter
    search_fields = ['name', 'last_name'] 
    ordering_fields = ['student_id', 'name', 'birth_date']
