from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # show username

    class Meta:
        model = Message
        fields = ["id", "group", "user", "text", "created_at"]
        read_only_fields = ["group", "user", "created_at"]
