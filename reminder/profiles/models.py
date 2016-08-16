#coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser	
from django.utils.translation import ugettext as _


class Profile(AbstractUser):
    name = models.CharField(max_length=50, verbose_name=_('Имя'))

    class Meta:
        verbose_name = _('Профиль')
        swappable = 'AUTH_USER_MODEL'
        verbose_name_plural = _('Профили')
