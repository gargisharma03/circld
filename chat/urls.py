from django.urls import path
from .views import group_messages

urlpatterns = [
    path('groups/<int:group_id>/messages/', group_messages, name='group-messages'),
]
