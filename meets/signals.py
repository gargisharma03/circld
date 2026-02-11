from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import RSVP


@receiver(post_save, sender=RSVP)
def auto_promote_waitlist(sender, instance, **kwargs):
    # Only trigger on cancel
    if instance.status != 'cancelled':
        return

    meet = instance.meet

    if meet.going_count < meet.capacity:
        waiting = RSVP.objects.filter(
            meet=meet,
            status='waiting'
        ).order_by('created_at').first()

        if waiting:
            waiting.status = 'going'
            waiting.save()
