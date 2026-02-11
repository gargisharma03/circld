from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Message, Group
from .serializers import MessageSerializer
from django.shortcuts import get_object_or_404

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def group_messages(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.method == "GET":
        messages = Message.objects.filter(group=group).order_by("-created_at")[:50]
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, group=group)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
