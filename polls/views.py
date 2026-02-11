from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Poll, PollOption
from .serializers import PollSerializer, PollOptionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from meets.models import Meet

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        poll = self.get_object()
        user = request.user
        option_id = request.data.get('option_id')

        try:
            option = poll.options.get(id=option_id)
        except PollOption.DoesNotExist:
            return Response({"detail": "Option not found"}, status=status.HTTP_404_NOT_FOUND)

        option.votes.add(user)
        return Response({"detail": "Vote recorded"})
    def finalize_poll(poll_id):
        poll = Poll.objects.get(id=poll_id)
        # pick the option with max votes
        best_option = max(poll.options.all(), key=lambda o: o.vote_count())
    
        # parse option text (you can use structured data instead of string)
        title = f"Meet for {poll.group.name}"
        location = "Parsed Location"
        date = "Parsed Date"
        time = "Parsed Time"

        meet = Meet.objects.create(
            title=title,
            group=poll.group,
            location=location,
            date=date,
            time=time,
            capacity=poll.group.max_members
        )

        poll.is_active = False
        poll.save()
        return meet
