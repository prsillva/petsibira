from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from blog.models import Animais, TipoAnimal, RacaAnimal
from adocao.models import Adotante
from despesas.models import Despesas, TipoDespesa
from doacao.models import Doador
from home.models import Sobre,Duvidas, Voluntarios
from funcionarios.models import Funcionarios
from funcionarios.models import Cargo
from .forms import AdmTipoDespesa, TodoForm, TpAnimal, AdotAnimal, SignUpForm, AdmDoacao, AdmFuncionarios, AdmCargo, AdmDespesa
from .forms import AddAnimal, RcAnimal, AdoteForm, AdmSobre, AdmDuvidas, AdmUser, AdmVoluntarios
from django.contrib.auth import login, authenticate
# specific to this view
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class adm (LoginRequiredMixin, generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'painel-adm.html'

@login_required
def TipoListView(request):    
    listar = TipoAnimal.objects.all()
    paginator = Paginator(listar, 5)
    page = request.GET.get('page')
    listar = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      listar = TipoAnimal.objects.filter(TipoAnimal__icontains = busca)

    return render(request, 'tipo-animal.html', {'list': listar})

@login_required
def DespesasListView(request):    
    listar = Despesas.objects.all()
    paginator = Paginator(listar, 5)
    page = request.GET.get('page')
    listar = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      listar = Despesas.objects.filter(TipoDespesa__icontains = busca)

    return render(request, 'list-despesas.html', {'list': listar})

@login_required
def MaioListView(request):    
    listar = Despesas.objects.all()
    paginator = Paginator(listar, 5)
    page = request.GET.get('page')
    listar = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      listar = Despesas.objects.filter(TipoDespesa__icontains = busca)

    return render(request, 'maio.html', {'list': listar})

@login_required
def MaioAniListView(request):    
    listar = Animais.objects.all()
    paginator = Paginator(listar, 5)
    page = request.GET.get('page')
    listar = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      listar = Despesas.objects.filter(TipoDespesa__icontains = busca)

    return render(request, 'animais-maio.html', {'list': listar})

@login_required
def JunhoAniListView(request):    
    listar = Animais.objects.all()
    paginator = Paginator(listar, 5)
    page = request.GET.get('page')
    listar = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      listar = Despesas.objects.filter(TipoDespesa__icontains = busca)

    return render(request, 'animais-junho.html', {'list': listar})

@login_required
def RelAnimaisListView(request):    
    listar = Animais.objects.all()
    paginator = Paginator(listar, 5)
    page = request.GET.get('page')
    listar = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      listar = Despesas.objects.filter(NomeAnimal__icontains = busca)

    return render(request, 'rel-animais.html', {'list': listar})

@login_required
def JunhoListView(request):    
    listar = Despesas.objects.all()
    paginator = Paginator(listar, 5)
    page = request.GET.get('page')
    listar = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      listar = Despesas.objects.filter(TipoDespesa__icontains = busca)

    return render(request, 'junho.html', {'list': listar})

@login_required
def RelListView(request):    
    listar = Despesas.objects.all()
    paginator = Paginator(listar, 5)
    page = request.GET.get('page')
    listar = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      listar = Despesas.objects.filter(TipoDespesa__icontains = busca)

    return render(request, 'rel-despesas.html', {'list': listar})


@login_required
def TipoDespesaListView(request):    
    listar = TipoDespesa.objects.all()
    paginator = Paginator(listar, 5)
    page = request.GET.get('page')
    listar = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca is not None:
    
      listar = TipoDespesa.objects.filter(TipoDespesa__TipoDespesa__icontains = busca)

    return render(request, 'list-tipodespesas.html', {'list': listar})

@login_required
def FuncListView(request):    
    listar = Funcionarios.objects.all()
    paginator = Paginator(listar, 5)
    page = request.GET.get('page')
    listar = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      listar = Funcionarios.objects.filter(Nome__icontains = busca)

    return render(request, 'list-funcionarios.html', {'list': listar})

@login_required
def CargoListView(request):    
    listar = Cargo.objects.all()
    paginator = Paginator(listar, 5)
    page = request.GET.get('page')
    listar = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      listar = Cargo.objects.filter(Cargo__icontains = busca)

    return render(request, 'list-cargo.html', {'list': listar})

@login_required
def DoacaoListView(request):    
    listar = Doador.objects.all()
    paginator = Paginator(listar, 5)
    page = request.GET.get('page')
    listar = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      listar = Doador.objects.filter(NomeDoador__icontains = busca)

    return render(request, 'list-doador.html', {'list': listar})


@login_required
def VoluntariosListView(request):    
    listar = Voluntarios.objects.all()
    paginator = Paginator(listar, 5)
    page = request.GET.get('page')
    listar = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      listar = Voluntarios.objects.filter(NomeVoluntario__icontains = busca)
    return render(request, 'list-voluntarios.html', {'list': listar})

@login_required
def AnimaisListView(request):    
    todoList = Animais.objects.all()
    paginator = Paginator(todoList, 5)
    page = request.GET.get('page')
    todoList = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      todoList = Animais.objects.filter(NomeAnimal__icontains = busca)
    return render(request, 'list-animais.html', {'list': todoList})



@login_required
def RacaListView(request):    
    raca = RacaAnimal.objects.all()
    paginator = Paginator(raca, 5)
    page = request.GET.get('page')
    raca = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      raca = RacaAnimal.objects.filter(RacaAnimal__icontains = busca)
    return render(request, 'raca-animal.html', {'raca': raca})

@login_required
def AdotanteListView(request):    
    adotante = Adotante.objects.all()
    paginator = Paginator(adotante, 5)
    page = request.GET.get('page')
    adotante = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      adotante = Adotante.objects.filter(AnimalAdotante__icontains = busca)
    return render(request, 'adotante.html', {'adotante': adotante})

@login_required
def UsersListView(request):    
    users = User.objects.all()
    paginac = Paginator(users, 5)
    page = request.GET.get('page')
    users = paginac.get_page(page)
    busca = request.GET.get('search')
    if busca:
      users = User.objects.filter(username__icontains = busca)
    return render(request, 'usuarios.html', {'users': users})

@login_required
def SobreListView(request):    
    sobre = Sobre.objects.all()
    paginator = Paginator(sobre, 5)
    page = request.GET.get('page')
    sobre = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      sobre = Sobre.objects.filter(titulo__icontains = busca)
    return render(request, 'list-sobre.html', {'sobre': sobre})

@login_required
def DuvidasListView(request):    
    duvidas = Duvidas.objects.all()
    paginator = Paginator(duvidas, 5)
    page = request.GET.get('page')
    duvidas = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
      duvidas = Duvidas.objects.filter(pergunta__icontains = busca)
    return render(request, 'duvidas-adm.html', {'duvidas': duvidas})

class reguser (generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registro.html'
    
@login_required
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            authenticate(username=username, password=raw_password)
            return redirect('/adm/usuarios/')
    else:
        form = SignUpForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def saveAction(request):
    print(request.POST)
    todoform = TodoForm(request.POST or None)

    if todoform.is_valid():
        todoform.save()

        return redirect('animais')
    return render(request, 'cadastro-animais.html', {'form': todoform})

@login_required
def editTodo(request, pk):

    pickTodo = Animais.objects.get(pk=pk)

    form = AddAnimal(request.POST or None, instance=pickTodo)

    if form.is_valid():
        form.save()
        return redirect('editar-animais.html')

    return render(request, 'editar-animais.html', {'list': form})

@login_required
def deleteAction(request, pk):

    pickTodo = Animais.objects.get(pk=pk)
    pickTodo.delete()

    return redirect('list-animais.html')

@login_required
def add_funcionario(request):
    form = AdmFuncionarios()

    if(request.method == 'POST'):

        form = AdmFuncionarios(request.POST, request.FILES)

        if(form.is_valid()):
            Nome = form.cleaned_data['Nome']
            Cpf = form.cleaned_data['Cpf']
            Telefone = form.cleaned_data['Telefone']
            Email = form.cleaned_data['Email']
            Cep = form.cleaned_data['Cep']
            Rua = form.cleaned_data['Rua']
            Bairro = form.cleaned_data['Bairro']
            Cidade = form.cleaned_data['Cidade']
            Estado = form.cleaned_data['Estado']
            
            Cargo = form.cleaned_data['Cargo']

            new_post = Funcionarios(Nome=Nome, Cpf=Cpf, Telefone=Telefone, Email=Email, Cep=Cep,Rua=Rua, Bairro=Bairro,Cidade=Cidade, Estado=Estado, Cargo=Cargo )
            new_post.save()

            return redirect('/adm/funcionarios/')
        else:
            return render(request, 'add-funcionario.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'add-funcionario.html', {'form': form})

@login_required
def add_despesas(request):
    form = AdmDespesa()

    if(request.method == 'POST'):

        form = AdmDespesa(request.POST, request.FILES)

        if(form.is_valid()):
            TipoDespesa  = form.cleaned_data['TipoDespesa']
            Descricao = form.cleaned_data['Descricao']
            Valor = form.cleaned_data['Valor']
            Quantidade = form.cleaned_data['Quantidade']
            Total = (Valor*Quantidade)
            


            new_post = Despesas(TipoDespesa=TipoDespesa, Descricao=Descricao, Valor=Valor, Quantidade=Quantidade, Total=Total)
            new_post.save()

            return redirect('/adm/despesas/')
        else:
            return render(request, 'add-despesas.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'add-despesas.html', {'form': form})

@login_required
def despesa_detalhes(request, id):
    list = Despesas.objects.get(id=id)
    return render(request, 'detalhes-despesa.html', {'list':list})

@login_required
def despesa_update(request,id):
    post = get_object_or_404(Despesas, pk=id)
    form = AdmDespesa(instance=post)


    if(request.method == 'POST'):
        form = AdmDespesa(request.POST, instance=post)

        if(form.is_valid()):
            post = form.save(commit=False)
            post.TipoDespesa = form.cleaned_data['TipoDespesa']
            post.Descricao = form.cleaned_data['Descricao']
            post.Valor = form.cleaned_data['Valor']
            post.Quantidade = form.cleaned_data['Quantidade']
            post.Total = (post.Valor*post.Quantidade)
            post.save()

            return redirect('/adm/despesas/')
        else:
            return render(request, 'edit-despesa.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'edit-despesa.html', {'form': form})


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
            SxAnimal = form.cleaned_data['SexoAnimal']
            Vdo = form.cleaned_data['Vacinado']
            Addo = form.cleaned_data['Adotado']
            FotoAnimal = form.cleaned_data['FotoCapaAnimal']
            Obs = form.cleaned_data['Observacao']

            new_post = Animais(NomeAnimal=NAnimal, IdadeAnimal=IdAnimal, TipoAnimal=TAnimal, RacaAnimal=RAnimal, PesoAnimal=PAnimal,CorAnimal=CAnimal, SexoAnimal=SxAnimal,Vacinado=Vdo, Adotado=Addo, FotoCapaAnimal=FotoAnimal, Observacao=Obs )
            new_post.save()

            return redirect('/adm/animais/')
        else:
            return render(request, 'cadastro-animais.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'cadastro-animais.html', {'form': form})

@login_required
def func_update(request,id):
    post = get_object_or_404(Funcionarios, pk=id)
    form = AdmFuncionarios(instance=post)


    if(request.method == 'POST'):
        form = AdmFuncionarios(request.POST, instance=post)

        if(form.is_valid()):
            post = form.save(commit=False)
            post.Nome = form.cleaned_data['Nome']
            post.Cpf = form.cleaned_data['Cpf']
            post.Telefone = form.cleaned_data['Telefone']
            post.Email = form.cleaned_data['Email']
            post.Cep = form.cleaned_data['Cep']
            post.Rua = form.cleaned_data['Rua']
            post.Bairro = form.cleaned_data['Bairro']
            post.Cidade = form.cleaned_data['Cidade']
            post.Estado = form.cleaned_data['Estado']            
            post.Cargo = form.cleaned_data['Cargo']
            post.save()

            return redirect('/adm/funcionarios/')
        else:
            return render(request, 'edit-funcionarios.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'edit-funcionarios.html', {'form': form})

@login_required
def post_update(request, id):
    post = get_object_or_404(Animais, pk=id)
    form = AddAnimal(instance=post)

    if(request.method == 'POST'):
        form = AddAnimal(request.POST, instance=post)
        
        if(form.is_valid()):
            post = form.save(commit=False)
            post.NAnimal = form.cleaned_data['NomeAnimal']
            post.IdAnimal = form.cleaned_data['IdadeAnimal']
            post.TAnimal = form.cleaned_data['TipoAnimal']
            post.RAnimal = form.cleaned_data['RacaAnimal']
            post.PAnimal = form.cleaned_data['PesoAnimal']
            post.CAnimal = form.cleaned_data['CorAnimal']
            post.SxAnimal = form.cleaned_data['SexoAnimal']
            post.Vdo = form.cleaned_data['Vacinado']
            post.Addo = form.cleaned_data['Adotado']
            post.FotoAnimal = form.cleaned_data['FotoCapaAnimal']
            post.Obs = form.cleaned_data['Observacao']

            post.save()

            return redirect('/adm/animais/')
        else:
            return render(request, 'editar-animais.html', {'form': form, 'post' : post})

    elif(request.method == 'GET'):
        return render(request, 'editar-animais.html', {'form': form, 'post' : post})

@login_required
def post_delete(request, id):
    post = get_object_or_404(Animais, pk=id)
    post.delete()
    return redirect('/adm/animais/')

def animais_detalhes(request, id):
    animais = Animais.objects.get(ativo=True, id=id)
    return render(request, 'detalhes-animais.html', {'animais':animais})

@login_required
def tipo_update(request, id):
    post = get_object_or_404(TipoAnimal, pk=id)
    form = TpAnimal(instance=post)

    if(request.method == 'POST'):
        form = TpAnimal(request.POST, instance=post)
        
        if(form.is_valid()):
            post = form.save(commit=False)
            post.TipoAnimal = form.cleaned_data['TipoAnimal']
            post.save()

            return redirect('/adm/animais/tipo/')
        else:
            return render(request, 'edittipo-animais.html', {'form': form, 'post' : post})

    elif(request.method == 'GET'):
        return render(request, 'edittipo-animais.html', {'form': form, 'post' : post})

@login_required
def tipo_delete(request, id):
    post = get_object_or_404(TipoAnimal, pk=id)
    post.delete()
    return redirect('/adm/animais/tipo/')

@login_required
def tipo_animal(request):
    form = TpAnimal()

    if(request.method == 'POST'):

        form = TpAnimal(request.POST, request.FILES)

        if(form.is_valid()):

            TAnimal = form.cleaned_data['TipoAnimal']
            new_post = TipoAnimal(TipoAnimal=TAnimal)
            new_post.save()

            return redirect('/adm/animais/')
        else:
            return render(request, 'tipo-animal.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'tipo-animal.html', {'form': form})

@login_required
def add_tipodespesa(request):
    form = AdmTipoDespesa()

    if(request.method == 'POST'):

        form = AdmTipoDespesa(request.POST, request.FILES)

        if(form.is_valid()):

            TpDespesa = form.cleaned_data['TipoDespesa']
            new_post = TipoDespesa(TipoDespesa=TpDespesa)
            new_post.save()

            return redirect('/adm/despesas/tipo/')
        else:
            return render(request, 'add-tipodespesa.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'add-tipodespesa.html', {'form': form})

@login_required
def add_tipo(request):
    form = TpAnimal()

    if(request.method == 'POST'):

        form = TpAnimal(request.POST, request.FILES)

        if(form.is_valid()):
            TAnimal = form.cleaned_data['TipoAnimal']


            new_post = TipoAnimal(TipoAnimal=TAnimal)
            new_post.save()

            return redirect('/adm/animais/tipo/')
        else:
            return render(request, 'add-tipo.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'add-tipo.html', {'form': form})

@login_required
def add_raca(request):
    form = RcAnimal()

    if(request.method == 'POST'):

        form = RcAnimal(request.POST, request.FILES)

        if(form.is_valid()):
            TipoAnimal = form.cleaned_data['TipoAnimal']
            RacAnimal = form.cleaned_data['RacaAnimal']
            new_post = RacaAnimal (TipoAnimal=TipoAnimal, RacaAnimal=RacAnimal)
            new_post.save()

            return redirect('/adm/animais/raca/')
        else:
            return render(request, 'add-raca.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'add-raca.html', {'form': form})
 
@login_required
def raca_delete (request, id):
        post = get_object_or_404(RacaAnimal, pk=id)
        post.delete()
        return redirect('/adm/animais/raca/')

@login_required
def raca_update(request, id):
    post = get_object_or_404(RacaAnimal, pk=id)
    form = RcAnimal(instance=post)

    if(request.method == 'POST'):
        form = RcAnimal(request.POST, instance=post)
        
        if(form.is_valid()):
            post = form.save(commit=False)
            post.TipoAnimal = form.cleaned_data['TipoAnimal']
            post.RacaAnimal = form.cleaned_data['RacaAnimal']
            post.save()

            return redirect('/adm/animais/raca/')
        else:
            return render(request, 'edit-raca.html', {'form': form, 'post' : post})

    elif(request.method == 'GET'):
        return render(request, 'edit-raca.html', {'form': form, 'post' : post})


@login_required
def add_adotante(request):
    form = AdoteForm()

    if(request.method == 'POST'):

        form = AdoteForm(request.POST, request.FILES)

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
            
            animais = Sobre(NomeAdotante=NomeAdotante, TelefoneAdotante=TelefoneAdotante, EmailAdotante=EmailAdotante, CepAdotante=CepAdotante, RuaAdotante=RuaAdotante,NumCasaAdotante=NumCasaAdotante, BairroAdotante=BairroAdotante, CidadeAdotante=CidadeAdotante, AnimalAdotante=AnimalAdotante, ObsAdotante=ObsAdotante )
            animais.save()
            return redirect('/adm/animais/adotante/')
        else:
            return render(request, 'add-adotante.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'add-adotante.html', {'form': form})
 
@login_required
def adotante_delete (request, id):
        post = get_object_or_404(Adotante, pk=id)
        post.delete()
        return redirect('/adm/animais/adotante/')

 
@login_required
def despesa_delete (request, id):
        post = get_object_or_404(Despesas, pk=id)
        post.delete()
        return redirect('/adm/despesas/')

@login_required
def adotante_update(request, id):
    post = get_object_or_404(Adotante, pk=id)
    form = AdoteForm(instance=post)

    if(request.method == 'POST'):
        form = AdoteForm(request.POST, instance=post)
        
        if(form.is_valid()):
            post = form.save(commit=False)
            post.NomeAdotante = form.cleaned_data['NomeAdotante']
            post.TelefoneAdotante = form.cleaned_data['TelefoneAdotante']
            post.EmailAdotante = form.cleaned_data['EmailAdotante']
            post.CepAdotante = form.cleaned_data['CepAdotante']
            post.RuaAdotante = form.cleaned_data['RuaAdotante']
            post.NumCasaAdotante = form.cleaned_data['NumCasaAdotante']
            post.BairroAdotante = form.cleaned_data['BairroAdotante']
            post.CidadeAdotante = form.cleaned_data['CidadeAdotante']
            post.AnimalAdotante = form.cleaned_data['AnimalAdotante']
            post.ObsAdotante = form.cleaned_data['ObsAdotante']

            return redirect('/adm/animais/adotante/')
        else:
            return render(request, 'edit-adotante.html', {'form': form, 'post' : post})

    elif(request.method == 'GET'):
        return render(request, 'edit-adotante.html', {'form': form, 'post' : post})

@login_required
def add_sobre(request):
    form = AdmSobre()

    if(request.method == 'POST'):

        form = AdmSobre(request.POST, request.FILES)

        if(form.is_valid()):
            titulo = form.cleaned_data['titulo']
            imagem_sobre = form.cleaned_data['imagem_sobre']
            texto_sobre = form.cleaned_data['texto_sobre']
            status = False
            animais = Sobre(titulo=titulo, imagem_sobre=imagem_sobre, texto_sobre=texto_sobre, status=status)
            animais.save()
            return redirect('/adm/animais/sobre/')
        else:
            return render(request, 'add-sobre.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'add-sobre.html', {'form': form})
 
@login_required
def sobre_delete (request, id):
        post = get_object_or_404(Sobre, pk=id)
        post.delete()
        return redirect('/adm/animais/sobre/')

@login_required
def sobre_update(request, id):
    post = get_object_or_404(Sobre, pk=id)
    form = AdmSobre(instance=post)

    if(request.method == 'POST'):
        form = AdmSobre(request.POST, instance=post)
        
        if(form.is_valid()):
            post = form.save(commit=False)
            post.titulo = form.cleaned_data['titulo']
            post.imagem_sobre = form.cleaned_data['imagem_sobre']
            post.texto_sobre = form.cleaned_data['texto_sobre']
            post.status = True
            post.save()
            return redirect('/adm/animais/sobre/')
        else:
            return render(request, 'edit-sobre.html', {'form': form, 'post' : post})

    elif(request.method == 'GET'):
        return render(request, 'edit-sobre.html', {'form': form, 'post' : post})

@login_required
def add_duvidas(request):
    form = AdmDuvidas()

    if(request.method == 'POST'):

        form = AdmDuvidas(request.POST, request.FILES)

        if(form.is_valid()):
            pergunta = form.cleaned_data['pergunta']
            texto_pergunta = form.cleaned_data['texto_pergunta']
            animais = Duvidas(pergunta=pergunta, texto_pergunta=texto_pergunta)
            animais.save()
            return redirect('/adm/animais/duvidas/')
        else:
            return render(request, 'add-duvidas.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'add-duvidas.html', {'form': form})
 
@login_required
def duvidas_delete (request, id):
        post = get_object_or_404(Duvidas, pk=id)
        post.delete()
        return redirect('/adm/animais/duvidas/')

@login_required
def duvidas_update(request, id):
    post = get_object_or_404(Duvidas, pk=id)
    form = AdmDuvidas(instance=post)

    if(request.method == 'POST'):
        form = AdmDuvidas(request.POST, instance=post)
        
        if(form.is_valid()):
            post = form.save(commit=False)
            post.pergunta = form.cleaned_data['pergunta']
            post.texto_pergunta = form.cleaned_data['texto_pergunta']
            post.save()
            return redirect('/adm/animais/duvidas/')
        else:
            return render(request, 'edit-duvidas.html', {'form': form, 'post' : post})

    elif(request.method == 'GET'):
        return render(request, 'edit-duvidas.html', {'form': form, 'post' : post})

@login_required
def user_delete (request, id):
        post = get_object_or_404(User, pk=id)
        post.delete()
        return redirect('/adm/usuarios/')

@login_required
def user_update(request, id):
    post = get_object_or_404(User, pk=id)
    form = AdmUser(instance=post)

    if(request.method == 'POST'):
        form = AdmUser(request.POST, instance=post)
        
        if(form.is_valid()):
            post = form.save(commit=False)
            post.first_name = form.cleaned_data['first_name']
            post.last_name = form.cleaned_data['last_name']
            post.email = form.cleaned_data['email']
            post.save()
            return redirect('/adm/usuarios/')
        else:
            return render(request, 'edit-user.html', {'form': form, 'post' : post})

    elif(request.method == 'GET'):
        return render(request, 'edit-user.html', {'form': form, 'post' : post})

@login_required
def add_voluntarios(request):
    form = AdmVoluntarios()

    if(request.method == 'POST'):

        form = AdmVoluntarios(request.POST, request.FILES)

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
            animais = Duvidas(NomeVoluntario=NomeVoluntario, TelefoneVoluntario=TelefoneVoluntario, EmailVoluntario=EmailVoluntario,IdadeVoluntario=IdadeVoluntario, TempoDisponivelHrsMes=TempoDisponivelHrsMes,CepVoluntario=CepVoluntario, RuaVoluntario=RuaVoluntario, NumCasaVoluntario=NumCasaVoluntario, BairroVoluntario=BairroVoluntario, CidadeVoluntario=CidadeVoluntario, MensagemVoluntario=MensagemVoluntario )
            animais.save()
            return redirect('/adm/voluntarios/')
        else:
            return render(request, 'add-voluntarios.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'add-voluntarios.html', {'form': form})
 
@login_required
def voluntarios_delete (request, id):
        post = get_object_or_404(Voluntarios, pk=id)
        post.delete()
        return redirect('/adm/voluntarios/')

@login_required
def voluntarios_update(request, id):
    post = get_object_or_404(Voluntarios, pk=id)
    form = AdmVoluntarios(instance=post)

    if(request.method == 'POST'):
        form = AdmVoluntarios(request.POST, instance=post)
        
        if(form.is_valid()):
            post.NomeVoluntario = form.cleaned_data['NomeVoluntario']
            post.TelefoneVoluntario = form.cleaned_data['TelefoneVoluntario']
            post.EmailVoluntario = form.cleaned_data['EmailVoluntario']
            post.IdadeVoluntario = form.cleaned_data['IdadeVoluntario']
            post.TempoDisponivelHrsMes = form.cleaned_data['TempoDisponivelHrsMes']
            post.CepVoluntario = form.cleaned_data['CepVoluntario']
            post.RuaVoluntario = form.cleaned_data['RuaVoluntario']
            post.NumCasaVoluntario = form.cleaned_data['NumCasaVoluntario']
            post.BairroVoluntario = form.cleaned_data['BairroVoluntario']
            post.CidadeVoluntario = form.cleaned_data['CidadeVoluntario']
            post.MensagemVoluntario = form.cleaned_data['MensagemVoluntario']
            post.save()
            return redirect('/adm/voluntarios/')
        else:
            return render(request, 'edit-voluntarios.html', {'form': form, 'post' : post})

    elif(request.method == 'GET'):
        return render(request, 'edit-voluntarios.html', {'form': form, 'post' : post})


@login_required
def add_doacao(request):
    form = AdmDoacao()

    if(request.method == 'POST'):

        form = AdmDoacao(request.POST, request.FILES)

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
            animais = Doador(NomeDoador=NomeDoador, TelefoneDoador=TelefoneDoador, EmailDoador=EmailDoador,TipoDoacao=TipoDoacao, QtdDoacao=QtdDoacao,CepDoador=CepDoador, RuaDoador=RuaDoador, NumeroCasaDoador=NumeroCasaDoador, BairroDoador=BairroDoador, CidadeDoador=CidadeDoador,EstadoDoador=EstadoDoador,  Observacao=Observacao )
            animais.save()
            return redirect('/adm/doacao/')
        else:
            return render(request, 'add-doacao.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'add-doacao.html', {'form': form})
 
@login_required
def doacao_delete (request, id):
        post = get_object_or_404(Doador, pk=id)
        post.delete()
        return redirect('/adm/doacao/')

@login_required
def doacao_update(request, id):
    post = get_object_or_404(Doador, pk=id)
    form = AdmDoacao(instance=post)

    if(request.method == 'POST'):
        form = AdmDoacao(request.POST, instance=post)
        
        if(form.is_valid()):
            post.NomeDoador = form.cleaned_data['NomeDoador']
            post.TelefoneDoador = form.cleaned_data['TelefoneDoador']
            post.EmailDoador = form.cleaned_data['EmailDoador']
            post.TipoDoacao = form.cleaned_data['TipoDoacao']
            post.QtdDoacao = form.cleaned_data['QtdDoacao']
            post.CepDoador = form.cleaned_data['CepDoador']
            post.RuaDoador = form.cleaned_data['RuaDoador']
            post.NumeroCasaDoador = form.cleaned_data['NumeroCasaDoador']
            post.BairroDoador = form.cleaned_data['BairroDoador']
            post.CidadeDoador = form.cleaned_data['CidadeDoador']
            post.EstadoDoador = form.cleaned_data['EstadoDoador']
            post.Observacao = form.cleaned_data['Observacao']
            post.save()
            return redirect('/adm/doacao/')
        else:
            return render(request, 'edit-doacao.html', {'form': form, 'post' : post})

    elif(request.method == 'GET'):
        return render(request, 'edit-doacao.html', {'form': form, 'post' : post})

@login_required
def add_cargo(request):
    form = AdmCargo()

    if(request.method == 'POST'):

        form = AdmCargo(request.POST, request.FILES)

        if(form.is_valid()):

            CargoName = form.cleaned_data['Cargo']
            new_post = Cargo(Cargo=CargoName)
            new_post.save()

            return redirect('/adm/cargo/')
        else:
            return render(request, 'add-cargo.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'add-cargo.html', {'form': form})

@login_required
def cargo_delete(request, id):
    post = get_object_or_404(Cargo, pk=id)
    post.delete()
    return redirect('/adm/cargo/')

@login_required
def cargo_update(request, id):
    post = get_object_or_404(Cargo, pk=id)
    form = AdmCargo(instance=post)

    if(request.method == 'POST'):
        form = AdmCargo(request.POST, instance=post)
        
        if(form.is_valid()):
            post = form.save(commit=False)
            post.Cargo = form.cleaned_data['Cargo']

            post.save()
            return redirect('/adm/cargo/')
        else:
            return render(request, 'edit-cargo.html', {'form': form, 'post' : post})

    elif(request.method == 'GET'):
        return render(request, 'edit-cargo.html', {'form': form, 'post' : post})