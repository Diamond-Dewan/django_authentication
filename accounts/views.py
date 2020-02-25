from django.utils import timezone
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from accounts.models import User
from accounts.forms import UserRegistrationForm


# Create your views here.
class UserRegister(CreateView):
    form_class = UserRegistrationForm
    template_name = 'forms/auth/sign_up.html'
    success_url = reverse_lazy('index')


class UsersListView(ListView):
    model = User
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        # base context
        context = super().get_context_data(**kwargs)
        # Add QuerySet from Foreign model
        # context['aricles'] = Aricle.objects.all()
        return context

