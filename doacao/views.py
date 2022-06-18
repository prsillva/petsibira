from django.shortcuts import redirect, render

from  home.forms import Voluntario
from .models import Doador
from .forms import DoadorForm

# Create your views here.

def doacao(request):
     return render(request, 'doador.html')

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
            
            return render(request, 'confirma-doacao.html', {'form': form})
        else:
            return render(request, 'doador.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'doador.html', {'form': form})

def voluntario(request):
    if request.method=='POST':
        form = Voluntario(request.POST)
        if form.is_valid():
            
            return redirect('/animais/')
        else:
            return render(request, 'doador.html', {'form': form})

    elif(request.method == 'GET'):
             return render(request, 'doador.html', {'form': form})
