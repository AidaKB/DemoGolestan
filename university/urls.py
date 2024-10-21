from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StudentListCreateAPIView, CoursesViewSet, TakesViewSet

router = DefaultRouter()
router.register(r'courses', CoursesViewSet, basename='courses')
router.register('takes', TakesViewSet, basename='takes')

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
]

urlpatterns += router.urls
