# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.urls import reverse

# Create your models here.

class DiaryEntry(models.Model):
    title = models.CharField(max_length=264)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('entry_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.text