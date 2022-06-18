from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Animais
from adocao.models import Adotante
from adocao.forms import AdotarForm
from .forms import AddAnimal
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, Http404
from django.http.response import HttpResponseNotAllowed
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render



class animais (generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'animais/listar-animais.html'

def confirmAdote(request):
    return render(request, 'confirma-adote.html')


def list_animais(request):
    list_animais = Animais.objects.filter(ativo=True).order_by('?')
    paginator = Paginator(list_animais, 10)

    page = request.GET.get('page')
    list = paginator.get_page(page)
    return render(request, 'listar-animais.html', {'list':list})


@login_required
def add_animal(request):
    form = AddAnimal()

    if(request.method == 'POST'):

        form = AddAnimal(request.POST, request.FILES)

        if(form.is_valid()):
            NAnimal = form.cleaned_data['NomeAnimal']
            IdAnimal = form.cleaned_data['IdadeAnimal']
            TAnimal = form.cleaned_data['TipoAnimal']
            RAnimal = form.cleaned_data['RacaAnimal']
            PAnimal = form.cleaned_data['PesoAnimal']
            CAnimal = form.cleaned_data['CorAnimal']
            Vdo = form.cleaned_data['Vacinado']
            Addo = form.cleaned_data['Adotado']
            FotoAnimal = form.cleaned_data['FotoCapaAnimal']
            Obs = form.cleaned_data['Observacao']

            new_post = Animais(NomeAnimal=NAnimal, IdadeAnimal=IdAnimal, TipoAnimal=TAnimal, RacaAnimal=RAnimal, PesoAnimal=PAnimal,CorAnimal=CAnimal, Vacinado=Vdo, Adotado=Addo, FotoCapaAnimal=FotoAnimal, Observacao=Obs )
            new_post.save()

            return redirect('/')
        else:
            return render(request, 'cadastro-animais.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'cadastro-animais.html', {'form': form})

@login_required
def animal_update(request, id):
    animal = get_object_or_404(Animais, pk=id)
    form = AddAnimal(instance=animal)

    if(request.method == 'POST'):
        form = AddAnimal(request.POST, instance=animal)
        
        if(form.is_valid()):
            animal = form.save(commit=False)
            animal.NAnimal = form.cleaned_data['NomeAnimal']
            animal.IdAnimal = form.cleaned_data['IdadeAnimal']
            animal.TAnimal = form.cleaned_data['TipoAnimal']
            animal.RAnimal = form.cleaned_data['RacaAnimal']
            animal.PAnimal = form.cleaned_data['PesoAnimal']
            animal.CAnimal = form.cleaned_data['CorAnimal']
            animal.Vdo = form.cleaned_data['Vacinado']
            animal.Addo = form.cleaned_data['Adotado']
            animal.FotoAnimal = form.cleaned_data['FotoCapaAnimal']
            animal.Obs = form.cleaned_data['PesoAnimal']

            animal.save()
            url = '/animais/detalhes/{}/'.format(animal.id)
            return redirect(url)
        else:
            return render(request, 'editar-animais.html', {'form': form, 'animal' : animal})

    elif(request.method == 'GET'):
        return render(request, 'editar-animais.html', {'form': form, 'animal' : animal})


def animais_detalhes(request, id):
    animais = Animais.objects.get(ativo=True, id=id)
    return render(request, 'detalhes-animais.html', {'animais':animais})

@login_required
def delete_animal(request, id):
    animais = Animais.objects.get(id=id)

    animais.delete()
    return redirect('/')

def register_pet(request, id):
    pet_id = request.GET.get(id=id)
    if pet_id:
        animais = Animais.objects.get(id=pet_id)
        return render(request, 'list-animais.html', {'animais':animais})
    return render(request, 'list-animais.html')

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
            return redirect('/animais/confirma-adocao/')
        else:
            return render(request, 'listar-animais.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'listar-animais.html', {'form': form})

class PessoaCreateView(CreateView):
        model = Adotante
        form_class = AdotarForm
        success_url = '/animais/'

   

