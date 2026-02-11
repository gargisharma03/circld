from django.db import models
from interests.models import Interest 
# Create your models here.
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    city = models.CharField(max_length=100)
    mbti = models.CharField(max_length=4, blank=True, null=True)
    activity_count = models.IntegerField(default=0)

    social_energy = models.CharField(
        max_length=10,
        choices=[
            ("low", "Low"),
            ("medium", "Medium"),
            ("high", "High"),
        ]
    )

    group_size_pref = models.CharField(
        max_length=10,
        choices=[
            ("3-5", "3-5"),
            ("6-10", "6-10"),
            ("10+", "10+"),
        ]
    )

    gender_pref = models.CharField(
        max_length=20,
        choices=[
            ("mixed", "Mixed"),
            ("same", "Same gender"),
        ]
    )

    is_verified = models.BooleanField(default=False)

    interests = models.ManyToManyField(Interest, blank=True)

    def __str__(self):
        return self.user.username


class Availability(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    weekdays = models.BooleanField(default=False)
    weekends = models.BooleanField(default=False)
    evenings = models.BooleanField(default=False)

