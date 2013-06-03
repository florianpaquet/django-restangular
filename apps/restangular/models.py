# -*- coding:utf-8 -*-
from django.db import models


class Item(models.Model):
    """
    Simple test item model
    """
    name = models.CharField(u"Name", max_length=255)

    def __unicode__(self):
        return self.name
