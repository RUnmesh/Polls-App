# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import question , choice

admin.site.register(question)
admin.site.register(choice)