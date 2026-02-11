

# Create your models here.
from django.db import models
from groups.models import Group
from django.contrib.auth.models import User

class Poll(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='polls')
    question = models.CharField(max_length=255)
    option_data = models.JSONField(default=dict)  
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)  # closes after Meet creation

    def __str__(self):
        return f"{self.title} ({self.group.name})"


class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=200)
    votes = models.ManyToManyField(User, related_name='poll_votes', blank=True)

    def vote_count(self):
        return self.votes.count()

    def __str__(self):
        return f"{self.option_text} ({self.poll.title})"
