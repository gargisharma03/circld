from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PollViewSet  # make sure this exists in polls/views.py

router = DefaultRouter()
router.register(r'', PollViewSet, basename='poll')

urlpatterns = [
    path('', include(router.urls)),
]
