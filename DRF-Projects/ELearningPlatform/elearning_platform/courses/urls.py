from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstructorViewSet, CourseViewSet, StudentViewSet, EnrollmentViewSet, LessonViewSet

router = DefaultRouter()
router.register("instructor", InstructorViewSet)
router.register("course", CourseViewSet)
router.register("student", StudentViewSet)
router.register("enrollment", EnrollmentViewSet)
router.register("lesson", LessonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]