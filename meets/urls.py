from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CreateMeetAPIView,
    GroupMeetListAPIView,
    RSVPAPIView,
    MarkAttendanceAPIView,
    FeedbackAPIView
)  # make sure this exists in meets/views.py

'''router = DefaultRouter()
router.register(r'', MeetViewSet, basename='meet')
'''
urlpatterns = [
    path("create/", CreateMeetAPIView.as_view()),
    path("group/<int:group_id>/", GroupMeetListAPIView.as_view()),
    path("<int:meet_id>/rsvp/", RSVPAPIView.as_view()),
    path("<int:meet_id>/attendance/", MarkAttendanceAPIView.as_view()),
    path("<int:meet_id>/feedback/", FeedbackAPIView.as_view()),
]