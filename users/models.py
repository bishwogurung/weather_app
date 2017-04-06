# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AnonymousUser
from django.db import models

class Guest(models.Model):
    user = AnonymousUser()