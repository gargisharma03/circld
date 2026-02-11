from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import Meet, RSVP, Attendance, Feedback
from .serializers import MeetSerializer, RSVPSerializer, AttendanceSerializer, FeedbackSerializer
from django.db import transaction
from rest_framework import status as http_status
from rest_framework.decorators import api_view, permission_classes




# ---------- Create Meet ----------
class CreateMeetAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MeetSerializer(data=request.data)
        if serializer.is_valid():
            meet = serializer.save(created_by=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# ---------- List Group Meets ----------
class GroupMeetListAPIView(APIView):
    def get(self, request, group_id):
        meets = Meet.objects.filter(group_id=group_id, is_active=True).order_by("date")
        return Response(MeetSerializer(meets, many=True).data)


# ---------- RSVP ----------
class RSVPAPIView(APIView):
    permission_classes = [IsAuthenticated]


    def post(self, request, meet_id):
        meet = get_object_or_404(Meet, id=meet_id)


        existing = RSVP.objects.filter(user=request.user, meet=meet).first()
        if existing:
            return Response({'detail': 'Already RSVPed'}, status=400)


        if meet.going_count >= meet.capacity:
            status_choice = 'waiting'
        else:
            status_choice = 'going'


        rsvp = RSVP.objects.create(
            user=request.user,
            meet=meet,
            status=status_choice
        )


        return Response({
            'status': status_choice,
            'message': 'RSVP successful'
        })

# ---------- Attendance ----------
class MarkAttendanceAPIView(APIView):
    def post(self, request, meet_id):
        meet = get_object_or_404(Meet, id=meet_id)

        attendance, _ = Attendance.objects.update_or_create(
            meet=meet,
            user=request.user,
            defaults={"attended": request.data.get("attended", True)}
        )

        return Response(AttendanceSerializer(attendance).data)


# ---------- Feedback ----------
class FeedbackAPIView(APIView):
    def post(self, request, meet_id):
        meet = get_object_or_404(Meet, id=meet_id)

        feedback, _ = Feedback.objects.update_or_create(
            meet=meet,
            user=request.user,
            defaults={
                "rating": request.data.get("rating"),
                "comment": request.data.get("comment", "")
            }
        )

        return Response(FeedbackSerializer(feedback).data)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def rsvp_meet(request, meet_id):
    user = request.user
    meet = get_object_or_404(Meet, id=meet_id, is_active=True)

    with transaction.atomic():

        existing = RSVP.objects.filter(user=user, meet=meet).first()
        if existing and existing.status != "cancelled":
            return Response({"detail": "Already RSVPed"}, status=400)

        going_count = RSVP.objects.filter(meet=meet, status="going").count()

        if going_count < meet.capacity:
            status_value = "going"
        else:
            status_value = "waiting"

        rsvp = RSVP.objects.create(
            user=user,
            meet=meet,
            status=status_value
        )

    return Response({
        "status": status_value,
        "message": "RSVP confirmed" if status_value=="going" else "Added to waitlist"
    }, status=201)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def cancel_rsvp(request, meet_id):
    user = request.user
    meet = get_object_or_404(Meet, id=meet_id)

    rsvp = RSVP.objects.filter(user=user, meet=meet).first()
    if not rsvp:
        return Response({"detail": "No RSVP found"}, status=404)

    rsvp.status = "cancelled"
    rsvp.save()

    # Auto-promote
    next_waiting = RSVP.objects.filter(
        meet=meet,
        status="waiting"
    ).order_by("created_at").first()

    if next_waiting:
        next_waiting.status = "going"
        next_waiting.save()

    return Response({"message": "RSVP cancelled and waitlist updated"})
