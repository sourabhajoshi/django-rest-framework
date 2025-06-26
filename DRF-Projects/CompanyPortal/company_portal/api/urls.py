from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.employee import DesignationViewSet, EmployeeViewSet

router = DefaultRouter()
router.register("designation", DesignationViewSet)
router.register('employee', EmployeeViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]