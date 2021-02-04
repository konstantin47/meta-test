from django.urls import path, include

from rest_framework import routers

from .views import PsychotherapistViewSet


router = routers.DefaultRouter()
router.register(r'', PsychotherapistViewSet, basename='psychotherapist')

urlpatterns = [
    path('', include(router.urls)),
]
