# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the ClockDetailView
    url(
        regex=r'^(?P<clock>[\w.@+-]+)/$',
        view=views.ClockDetailView.as_view(),
        name='detail'
    ),
]
