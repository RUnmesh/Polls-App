# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class question(models.Model) :
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self) :
        return self.text

class choice(models.Model) :
    question = models.ForeignKey( question , on_delete = models.CASCADE )
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)

    def __str__(self) :
        return self.text
