from django.db import models
from django.conf import settings
from interests.models import Interest
from django.contrib.auth.models import User

class Group(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('locked', 'Locked'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    goal = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    max_members = models.PositiveIntegerField(default=5)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    gender_pref = models.CharField(max_length=10, blank=True, null=True)
    age_range = models.CharField(max_length=20, blank=True, null=True)

    members = models.ManyToManyField(
        User, through='GroupMember', related_name='group_memberships', blank=True
    )
    interests = models.ManyToManyField(Interest, related_name='groups', blank=True)
    admins = models.ManyToManyField(User, related_name='admin_groups', blank=True)

    def __str__(self):
        return self.name



class GroupMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "group")

    def __str__(self):
        return f"{self.user.username} in {self.group.name}"
