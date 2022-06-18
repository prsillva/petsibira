from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class register (generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = '/adm/usuarios/'