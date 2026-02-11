# groups/serializers.py
# groups/serializers.py
from rest_framework import serializers
from .models import Group
from meets.models import Meet
from polls.models import Poll
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]  # pick whatever you need

class GroupSerializer(serializers.ModelSerializer):
    # optional: nested user serializer for admins/members
    admins = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True
    )
    members = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True
    )
    interests = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.none(), many=True
    )  # replace with your Interest model if you have one

    class Meta:
        model = Group
        fields = '__all__'

    def create(self, validated_data):
        # pop M2M fields first
        admins_data = validated_data.pop('admins', [])
        members_data = validated_data.pop('members', [])
        interests_data = validated_data.pop('interests', [])

        # Step 1: Save the group to DB → gets an ID in PostgreSQL
        group = Group.objects.create(**validated_data)

        # Step 2: Set M2M fields now that group has an ID
        if admins_data:
            group.admins.set(admins_data)
        if members_data:
            group.members.set(members_data)
        if interests_data:
            group.interests.set(interests_data)

        # Step 3: Optional logic
        if group.members.count() >= group.max_members:
            group.status = 'locked'
            group.save(update_fields=['status'])

        return group
class MeetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meet
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

class GroupReadSerializer(serializers.ModelSerializer):
    meets = MeetSerializer(many=True, read_only=True)
    polls = PollSerializer(many=True, read_only=True)
    
    class Meta:
        model = Group
        fields = '__all__'
class SuggestedGroupSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'score']  # include all fields you need

    def get_score(self, obj):
        # The view should attach a temporary `_score` attribute
        return getattr(obj, '_score', 0)