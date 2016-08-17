from __future__ import unicode_literals
from profiles.models import Profile
from note.models import Reminder
from django.db import models
from django.utils import timezone


class Comment(models.Model):
    author = models.ForeignKey(Profile, blank=True, null=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_of_publish = models.DateTimeField(default=timezone.now())
    reminder = models.ForeignKey(Reminder, default=None, null=True, blank=True, related_name='comments')

    def __unicode__(self):
        return self.title
