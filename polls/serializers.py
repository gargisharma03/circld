from rest_framework import serializers
from .models import Poll, PollOption

class PollOptionSerializer(serializers.ModelSerializer):
    vote_count = serializers.IntegerField(source='vote_count', read_only=True)

    class Meta:
        model = PollOption
        fields = ['id', 'option_text', 'vote_count']

class PollSerializer(serializers.ModelSerializer):
    options = PollOptionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'group', 'created_by', 'is_active', 'options']

    def create(self, validated_data):
        options_data = validated_data.pop('options')
        poll = Poll.objects.create(**validated_data)
        for option in options_data:
            PollOption.objects.create(poll=poll, **option)
        return poll
