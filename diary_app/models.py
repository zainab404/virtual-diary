# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.urls import reverse

# Create your models here.

class DiaryEntry(models.Model):
    title = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()

    def publish(self):
        self.published_date(timezone.now())
        self.save()

    # def get_absolute_url(self):
    #     pass

    def __str__(self):
        return self.title
    



