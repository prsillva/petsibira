from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Adotante
from .forms import AdotarForm
from blog.models import Animais

# Create your views here.
@login_required
def adotar_animal(request):
    form = AdotarForm()
    if(request.method == 'POST'):

        form = AdotarForm(request.POST)

        if(form.is_valid()):
            
            NomeAdotante = form.cleaned_data['NomeAdotante']
            TelefoneAdotante = form.cleaned_data['TelefoneAdotante']
            EmailAdotante = form.cleaned_data['EmailAdotante']
            CepAdotante = form.cleaned_data['CepAdotante']
            RuaAdotante = form.cleaned_data['RuaAdotante']
            NumCasaAdotante = form.cleaned_data['NumCasaAdotante']
            BairroAdotante = form.cleaned_data['BairroAdotante']
            CidadeAdotante = form.cleaned_data['CidadeAdotante']
            AnimalAdotante = form.cleaned_data['AnimalAdotante']
            ObsAdotante = form.cleaned_data['ObsAdotante']
            
            animais = Adotante(NomeAdotante=NomeAdotante, TelefoneAdotante=TelefoneAdotante, EmailAdotante=EmailAdotante, CepAdotante=CepAdotante, RuaAdotante=RuaAdotante,NumCasaAdotante=NumCasaAdotante, BairroAdotante=BairroAdotante, CidadeAdotante=CidadeAdotante, AnimalAdotante=AnimalAdotante, ObsAdotante=ObsAdotante )
            animais.save()
            return redirect('/animais/')
        else:
            return render(request, 'adotar.html', {'animais': animais})

    elif(request.method == 'GET'):
        return render(request, 'adotar.html', {'animais': animais})
    
def register_pet(request):
    pet_id = request.GET.get('id')
    if pet_id:
        pet = Animais.objects.get(id=pet_id)
        return render(request, 'list-animais.html', {'pet':pet})
    return render(request, 'list-animais.html')