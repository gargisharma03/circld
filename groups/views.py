from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Group, GroupMember
from .serializers import GroupSerializer,GroupReadSerializer
from rest_framework import generics
from django.db.models import F
from .serializers import SuggestedGroupSerializer
from accounts.models import Profile
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from polls.models import Poll, PollOption


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        group = self.get_object()
        user = request.user
        if group.is_locked:
            return Response({"detail": "Group is full/locked"}, status=status.HTTP_400_BAD_REQUEST)
        member, created = GroupMember.objects.get_or_create(user=user, group=group)
        group.update_lock_status()
        return Response({"detail": "Joined successfully"})

    @action(detail=True, methods=['post'])
    def leave(self, request, pk=None):
        group = self.get_object()
        user = request.user
        GroupMember.objects.filter(user=user, group=group).delete()
        group.update_lock_status()
        return Response({"detail": "Left group successfully"})
    @action(detail=True, methods=['post'])
    def spark(self, request, pk=None):
        """
        Spark button: creates a Poll for Meet options.
        """
        group = self.get_object()
        user = request.user

        # Create a poll automatically
        poll = Poll.objects.create(
            group=group,
            title="Spark: Decide Meet",
            description="Vote for preferred date/time/location",
            created_by=user
        )

        # Example default options, in real app let user provide suggestions
        default_options = ["Tomorrow 6 PM at Cafe A", "Saturday 4 PM at Park B", "Sunday 10 AM at Library"]
        for opt in default_options:
            PollOption.objects.create(poll=poll, option_text=opt)

        return Response({"detail": "Poll created for Spark", "poll_id": poll.id})
class GroupListView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupReadSerializer

class GroupSuggestionsView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        profile = get_object_or_404(Profile, user__id=user_id)

        groups = Group.objects.all()
        suggestions = []

        for group in groups:
            # Get members and their profiles
            members = GroupMember.objects.filter(group=group)
            member_profiles = Profile.objects.filter(user__in=members.values_list('user_id', flat=True))

            # Interest overlap
            user_interests = set(profile.interests.values_list('id', flat=True))

            member_interest_matches = 0
            for member_profile in member_profiles:
                member_interests = set(member_profile.interests.values_list('id', flat=True))
                if user_interests:
                    member_interest_matches += len(user_interests & member_interests) / len(user_interests)

            # average similarity across members
            interest_score = member_interest_matches / max(member_profiles.count(), 1)

            # Location score: fraction of members in same city
            location_score = member_profiles.filter(city=profile.city).count() / max(member_profiles.count(), 1) if member_profiles.exists() else 0

            # MBTI score: fraction of members with same MBTI
            mbti_score = member_profiles.filter(mbti=profile.mbti).count() / max(member_profiles.count(), 1) if member_profiles.exists() else 0

            # Activity level
            group_activity = GroupMember.objects.filter(group=group).count()
            activity_score = min(group_activity / 50, 1)  # 50 = normalization constant

            # Weighted total score
            score = 0.4*interest_score + 0.3*location_score + 0.2*mbti_score + 0.1*activity_score

            suggestions.append({
                'group': group,
                'score': score
            })

        # Top 10
        suggestions = sorted(suggestions, key=lambda x: x['score'], reverse=True)[:10]
        for s in suggestions:
            s['group']._score = s['score']  # attach temporary attribute

        serializer = SuggestedGroupSerializer([s['group'] for s in suggestions], many=True)
        data = serializer.data

        for i, s in enumerate(suggestions):
            data[i]['score'] = round(s['score'], 3)

        return Response(data)

