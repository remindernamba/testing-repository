#coding: utf-8
from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models
from profiles.models import Profile
from django.utils import timezone


class Group(models.Model):
    user = models.ManyToManyField(Profile, verbose_name=_('Профиль'), default=None, null=True, blank=True, related_name='profile')
    name = models.CharField(max_length=50, verbose_name=_('Название'), default=None, null=True)

    def __unicode__(self):
        return unicode(self.name) or u''

    class Meta:
        verbose_name = _('Группа')
        verbose_name_plural = _('Группы')


class Reminder(models.Model):
    user = models.ManyToManyField(Profile, verbose_name=_('Профиль'), default=None, null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=_('Название'), default=None, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    date_of_publish = models.DateTimeField(verbose_name=_('Дата Публикации'), default=timezone.now(), null=True, blank=True)
    date_of_start = models.DateTimeField(verbose_name=_('Дата Публикации'), default=timezone.now(), null=True, blank=True)
    group = models.ForeignKey(Group, verbose_name=_('Группа'), related_name='reminder')

    def __unicode__(self):
        return unicode(self.name) or u''

    class Meta:
        verbose_name = _('Напоминание')
        verbose_name_plural = _('Напоминании')
