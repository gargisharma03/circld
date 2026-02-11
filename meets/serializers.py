from rest_framework import serializers
from .models import Meet, RSVP, Attendance, Feedback

class MeetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meet
        fields = '__all__'
    def get_rsvp_count(self, obj):
        return obj.rsvps.filter(status="going").count()


class RSVPSerializer(serializers.ModelSerializer):
    class Meta:
        model = RSVP
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"