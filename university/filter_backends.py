from django_filters import rest_framework as filters
from .models import Student


class StudentFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    student_id = filters.NumberFilter()

    class Meta:
        model = Student
        fields = ['name', 'last_name', 'student_id', 'birth_date']
