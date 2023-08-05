# resumes/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CVViewSet

router = DefaultRouter()
router.register(r'cv', CVViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
