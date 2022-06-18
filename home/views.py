from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from blog.models import Animais
from doacao.models import Doador
from django.core.paginator import Paginator
from home.models import Sobre, Duvidas, Voluntarios
from .forms import AddVoluntario, DoadorForm


def home(request):
    animais = Animais.objects.filter(ativo=True).order_by('?')[:3]
    template = loader.get_template('index.html')
    context = {
        'animais': animais,
    }
    return new_func(request, template, context)

def new_func(request, template, context):
    return HttpResponse(template.render(context, request))

def sobre(request):
    lista_sobre = Sobre.objects.filter(status=True)[:1]
    template = loader.get_template('sobre.html')
    context = {
        'lista_sobre': lista_sobre,
    }
    return new_func(request, template, context)

def listar_animais(request):
    animais = Animais.objects.filter(ativo=True).order_by('?')
    paginator = Paginator(animais, 3)
    page = request.GET.get('page')
    animais = paginator.get_page(page)
    return render(request, 'listar-animais.html', {'animais':animais})

def duvidas(request):
    lista_duvidas = Duvidas.objects.all()[:10]
    template = loader.get_template('duvidas.html')
    context = {
        'lista_duvidas': lista_duvidas,
    }
    return new_func(request, template, context)
   

def voluntarios(request):
    form = AddVoluntario()

    if(request.method == 'POST'):

        form = AddVoluntario(request.POST, request.FILES)

        if(form.is_valid()):
            NomeVoluntario = form.cleaned_data['NomeVoluntario']
            TelefoneVoluntario = form.cleaned_data['TelefoneVoluntario']
            EmailVoluntario = form.cleaned_data['EmailVoluntario']
            IdadeVoluntario = form.cleaned_data['IdadeVoluntario']
            TempoDisponivelHrsMes = form.cleaned_data['TempoDisponivelHrsMes']
            CepVoluntario = form.cleaned_data['CepVoluntario']
            RuaVoluntario = form.cleaned_data['RuaVoluntario']
            NumCasaVoluntario = form.cleaned_data['NumCasaVoluntario']
            BairroVoluntario = form.cleaned_data['BairroVoluntario']
            CidadeVoluntario = form.cleaned_data['CidadeVoluntario']
            MensagemVoluntario = form.cleaned_data['MensagemVoluntario']

            new_post = Voluntarios(NomeVoluntario=NomeVoluntario, TelefoneVoluntario=TelefoneVoluntario, EmailVoluntario=EmailVoluntario, IdadeVoluntario=IdadeVoluntario,TempoDisponivelHrsMes=TempoDisponivelHrsMes, CepVoluntario=CepVoluntario,RuaVoluntario=RuaVoluntario, NumCasaVoluntario=NumCasaVoluntario, BairroVoluntario=BairroVoluntario, CidadeVoluntario=CidadeVoluntario, MensagemVoluntario=MensagemVoluntario )
            new_post.save()

            return render(request, 'confirma-voluntario.html', {'form': form})
        else:
            return render(request, 'voluntarios.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'voluntarios.html', {'form': form})

def doar_animal(request):
    form = DoadorForm()

    if(request.method == 'POST'):

        form = DoadorForm(request.POST, request.FILES)

        if(form.is_valid()):
            NomeDoador = form.cleaned_data['NomeDoador']
            TelefoneDoador = form.cleaned_data['TelefoneDoador']
            EmailDoador = form.cleaned_data['EmailDoador']
            TipoDoacao = form.cleaned_data['TipoDoacao']
            QtdDoacao = form.cleaned_data['QtdDoacao']
            CepDoador = form.cleaned_data['CepDoador']
            RuaDoador = form.cleaned_data['RuaDoador']
            NumeroCasaDoador = form.cleaned_data['NumeroCasaDoador']
            BairroDoador = form.cleaned_data['BairroDoador']
            CidadeDoador = form.cleaned_data['CidadeDoador']
            EstadoDoador = form.cleaned_data['EstadoDoador']
            Observacao = form.cleaned_data['Observacao']
            DeAcordoDoador = form.cleaned_data['DeAcordoDoador']

            new_post = Doador(NomeDoador=NomeDoador, TelefoneDoador=TelefoneDoador, EmailDoador=EmailDoador, TipoDoacao=TipoDoacao, QtdDoacao=QtdDoacao,CepDoador=CepDoador, RuaDoador=RuaDoador, NumeroCasaDoador=NumeroCasaDoador, BairroDoador=BairroDoador,CidadeDoador=CidadeDoador, EstadoDoador=EstadoDoador, Observacao=Observacao, DeAcordoDoador=DeAcordoDoador )
            new_post.save()
            
            return redirect('/animais/')
        else:
            return render(request, 'doador.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'doador.html', {'form': form})
