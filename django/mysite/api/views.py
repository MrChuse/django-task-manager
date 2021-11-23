import os
import json

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login

from .models import Task
from .forms import TaskForm
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'index.html'
    def get_queryset(self):
        return Task.objects.order_by('-end_date')
    

class ProfileView(generic.ListView):
    template_name = 'profile.html'
    def get_queryset(self):
        req = self.request
        usr = req.user
        return Task.objects.filter(users=self.request.user).order_by('-end_date')

class DetailView(generic.DetailView):
    model = Task
    template_name = 'detail.html'

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            users = form.cleaned_data.pop('users')
            task = Task(**form.cleaned_data)
            task.save()
            task.users.set(users)
            task.save()
            return HttpResponseRedirect('/')
    else:
        form = TaskForm()

    return render(request, 'create_task_form.html', {'form': form})
        
def create_user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(**form.cleaned_data)
                login(request, user)
            except IntegrityError:
                return render(request, 'create_user_form.html', {
                'error_message': "The user already exists.",
                'form': form
               })
            return HttpResponseRedirect('/accounts/profile/')
    else:
        form = UserForm()

    return render(request, 'create_user_form.html', {'form': form})
