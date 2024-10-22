from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StudentListCreateAPIView, CoursesViewSet, TakesViewSet, TeacherListCreateAPIView

router = DefaultRouter()
router.register(r'courses', CoursesViewSet, basename='courses')
router.register('takes', TakesViewSet, basename='takes')

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('teachers/', TeacherListCreateAPIView.as_view(), name='teacher-list-create')
]

urlpatterns += router.urls
