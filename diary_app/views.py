# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import DiaryEntry
from .forms import NewEntryForm, UserForm
# Create your views here.
def index(request): 
    return render(request, 'index.html')

def register(request):
    registered = False

    if request.method == "POST":
        userform = UserForm(data=request.POST)

        if userform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
            #if the user has a proper username and password, then the registered variable becomes true.
            registered = True        
        else:
            print(userform.errors)
    else:
        userform = UserForm()
    
    return render(request, 'diary_app/registration.html', context={'userform':userform, 'registered':registered})
        
def user_login(request):
    #^^^'login' is a special word so make sure to make it different.
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        #^^^LOOK INTO THIS METHOD FOR RESEARCH

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print("Login Attempt Created! Diary is comprimised.")
            print("Attempt - Username: {} Password: {}".format(username,password))
            return HttpResponse("Invalid Login Details. Try Again.")
    else:
        return render(request, 'diary_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index')) 

class CreateEntry(CreateView, LoginRequiredMixin):
    template_name = 'new_entry.html'
    login_url = '/login/'
    #^^^LOOK INTO WHAT THIS DOES IN TERMS OF DJANGO
    redirect_field_name = 'diary_app/index.html'
    form_class = NewEntryForm
    model = DiaryEntry

class EntryDetail(DetailView, LoginRequiredMixin):
    template_name = 'entry_detail.html'
    login_url = '/login/'
    model = DiaryEntry

@login_required
def publish_entry(request, pk):
    print("======Publishing from views======")
    specific_entry = get_object_or_404(DiaryEntry, pk=pk)
    specific_entry.publish()
    return redirect('entry_detail', pk=specific_entry.pk)

# class EntryList(ListView, LoginRequiredMixin):
#     login_url = '/login/'
#     model = DiaryEntry

#     def get_queryset(self):
#         return DiaryEntry.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

# class DraftList(ListView, LoginRequiredMixin):
#     login_url = '/login/'
#     redirect_field_name = 'entry_list.html'
#     model = DiaryEntry

#     def get_queryset(self):
#         return DiaryEntry.objects.filter(published_date__isnull=True).order_by('-published_date')


# class UpdateEntry(UpdateView, LoginRequiredMixin):
#     login_url = '/login/'
#     redirect_field_name = 'diary_app/entry_detail.html'
#     form_class = NewEntryForm
#     model = DiaryEntry


# class DeleteEntry(DeleteView, LoginRequiredMixin):
#     model = DiaryEntry
#     success_url = reverse_lazy('entry_list')
#     #^how come its not 'diary/entry_list'


