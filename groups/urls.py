from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, GroupSuggestionsView

router = DefaultRouter()
router.register(r'', GroupViewSet, basename='group')

urlpatterns = [
    path('suggestions/', GroupSuggestionsView.as_view(), name='group-suggestions'),  # <- just 'suggestions/' here
    path('', include(router.urls)), 
]
