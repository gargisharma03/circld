from django.contrib import admin
from .models import Meet, RSVP, Attendance, Feedback

admin.site.register(Meet)
admin.site.register(RSVP)
admin.site.register(Attendance)
admin.site.register(Feedback)
