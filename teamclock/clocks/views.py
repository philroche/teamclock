# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView


from .models import Clock


class ClockDetailView(DetailView):
    model = Clock
    # These next two lines tell the view to index lookups by username
    slug_field = "uid"
    slug_url_kwarg = "clock"

