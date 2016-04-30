# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from timezone_field import TimeZoneField

@python_2_unicode_compatible
class Clock(models.Model):
    name = models.CharField(_("Name of Clock"), blank=False, max_length=255)
    uid = models.CharField(_("Unique identifier of Clock"), blank=False, max_length=255)


    def __str__(self):
        return '%s-%s' % (self.uid, self.name)


@python_2_unicode_compatible
class TeamMember(models.Model):
    name = models.CharField(_("Name of Team Member"), blank=False, max_length=255)
    clock = models.ForeignKey(Clock, null=False, blank=False)
    timezone = TimeZoneField(default='Europe/London')  # defaults supported
    city = models.CharField(_("City of Team Member"), blank=False, max_length=255)
    color = models.CharField(_("Color (HEX)"), blank=False, max_length=7, default="#EEEEEE")

    def __str__(self):
        return '%s from clock %s' % (self.name, self.clock.name)
