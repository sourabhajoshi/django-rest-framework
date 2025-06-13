from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, JobPostingViewSet, ApplicationViewSet, ApplicantViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('companies', CompanyViewSet)
router.register('jobs', JobPostingViewSet)
router.register('applicants', ApplicantViewSet)
router.register('applications', ApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]