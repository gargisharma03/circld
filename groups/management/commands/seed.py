from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile
from groups.models import Group, GroupMember
from accounts.models import Interest
import random

class Command(BaseCommand):
    help = "Seed database with dummy data for Circld"

    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.WARNING("🌱 Seeding database..."))

        # ---------- Interests ----------
        interest_names = [
            "AI", "Startups", "Design", "Fitness", "Mental Health",
            "Books", "Travel", "Finance", "Coding", "Gaming"
        ]

        interests = []
        for name in interest_names:
            obj, _ = Interest.objects.get_or_create(name=name)
            interests.append(obj)

        self.stdout.write(self.style.SUCCESS("✓ Interests created"))

        # ---------- Users + Profiles ----------
        cities = ["Delhi", "Mumbai", "Bangalore", "Pune"]
        mbtis = ["INTJ", "ENTP", "INFJ", "ISTP", "ENFP", "ISFJ"]

        users = []

        for i in range(1, 11):
            user, created = User.objects.get_or_create(
                username=f"user{i}",
                defaults={"email": f"user{i}@test.com"}
            )
            if created:
                user.set_password("test1234")
                user.save()

            profile, _ = Profile.objects.get_or_create(
                user=user,
                defaults={
                    "city": random.choice(cities),
                    "mbti": random.choice(mbtis),
                    "activity_count": random.randint(5, 80)
                }
            )

            profile.interests.set([i.id for i in random.sample(interests, random.randint(2, 4))])
            users.append(user)

        self.stdout.write(self.style.SUCCESS("✓ Users & Profiles created"))

        # ---------- Groups ----------
        group_data = [
            ("Founders Circle", "Startup builders", "Delhi"),
            ("Mindful Humans", "Mental health & growth", "Mumbai"),
            ("Code Collective", "Developers hub", "Bangalore"),
            ("Bookoholics", "Readers club", "Pune"),
            ("Fit Tribe", "Fitness & wellness", "Delhi"),
            ("Design Den", "Designers space", "Bangalore"),
        ]

        groups = []

        for name, desc, city in group_data:
            group, _ = Group.objects.get_or_create(
                name=name,
                defaults={
                    "description": desc,
                    "city": city
                }
            )
            group.interests.set([i.id for i in random.sample(interests, random.randint(2, 4))])
            groups.append(group)

        self.stdout.write(self.style.SUCCESS("✓ Groups created"))

        # ---------- Group Members ----------
        for group in groups:
            members = random.sample(users, random.randint(2, 6))
            for user in members:
                GroupMember.objects.get_or_create(user=user, group=group)

        self.stdout.write(self.style.SUCCESS("✓ Group members linked"))

        self.stdout.write(self.style.SUCCESS("🔥 Database seeding complete. Circld now has a brain."))
