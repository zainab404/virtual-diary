# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import DiaryEntry
from .forms import NewEntryForm
# Create your views here.
def index(request): 
    return render(request, 'index.html')

class EntryList(ListView, LoginRequiredMixin):
    login_url = '/login/'
    model = DiaryEntry

    def get_queryset(self):
        return DiaryEntry.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

# class EntryDetail(DetailView, LoginRequiredMixin):
#     login_url = '/login/'
#     model = DiaryEntry

# class CreateEntry(CreateView, LoginRequiredMixin):
#     login_url = '/login/'
#     redirect_field_name = 'diary_app/entry_detail.html'
#     form_class = NewEntryForm
#     model = DiaryEntry

# class UpdateEntry(UpdateView, LoginRequiredMixin):
#     login_url = '/login/'
#     redirect_field_name = 'diary_app/entry_detail.html'
#     form_class = NewEntryForm
#     model = DiaryEntry


# class DeleteEntry(DeleteView, LoginRequiredMixin):
#     model = DiaryEntry
#     success_url = reverse_lazy('entry_list')
#     #^how come its not 'diary/entry_list'

# class DraftList(ListView, LoginRequiredMixin):
#     login_url = '/login/'
#     redirect_field_name = 'entry_list.html'
#     model = DiaryEntry

#     def get_queryset(self):
#         return DiaryEntry.objects.filter(published_date__isnull=True).order_by('-published_date')

# @login_required
# def publish_entry(request, pk):
#     specific_entry = get_object_or_404(DiaryEntry, pk=pk)
#     specific_entry.publish()
#     return redirect('entry_detail.html', pk=post.pk)

