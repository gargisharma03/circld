from django.db import models
from django.contrib.auth.models import User
from groups.models import Group
from django.utils import timezone

class Meet(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="meets")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    @property
    def going_count(self):
        return self.rsvps.filter(status='going').count()

    def __str__(self):
        return f"{self.title} | {self.group.name}"


class RSVP(models.Model):
    STATUS_CHOICES = [
        ("going", "Going"),
        ("maybe", "Maybe"),
        ("not_going", "Not Going"),
    ]

    meet = models.ForeignKey(Meet, on_delete=models.CASCADE, related_name="rsvps")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("meet", "user")


class Attendance(models.Model):
    meet = models.ForeignKey(Meet, on_delete=models.CASCADE, related_name="attendance")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attended = models.BooleanField(default=False)
    marked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("meet", "user")


class Feedback(models.Model):
    meet = models.ForeignKey(Meet, on_delete=models.CASCADE, related_name="feedbacks")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()  # 1–5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("meet", "user")
