from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Event(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length=100, default='general')
    tags = models.JSONField(default=list)
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=100, default='general')  # platform / community / public
    verified = models.BooleanField(default=False)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
