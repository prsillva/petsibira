from blog.models import Animais, TipoAnimal, RacaAnimal
from home.models import Duvidas
from adocao.models import Adotante
from django import forms

from home.models import Sobre
from django.forms import ModelForm, TextInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from home.models import Voluntarios
from doacao.models import Doador
from funcionarios.models import Funcionarios, Cargo
from despesas.models import Despesas, TipoDespesa



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Teste.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class TodoForm(ModelForm):
    class Meta:
        model = Animais
        #fields = ['content', 'added_time']
        fields = '__all__'

class AdmTipoDespesa(ModelForm):
    class Meta:
        model = TipoDespesa
        #fields = ['content', 'added_time']
        fields = '__all__'

class AdmDespesa(ModelForm):
    class Meta:
        model = Despesas
        #fields = ['content', 'added_time']
        fields = ['TipoDespesa', 'Descricao','Valor','Quantidade']


class AddAnimal(ModelForm):
    class Meta:
        model = Animais
        fields = ['NomeAnimal', 'IdadeAnimal', 'TipoAnimal', 'RacaAnimal', 'PesoAnimal','CorAnimal', 'SexoAnimal','Vacinado', 'Adotado', 'FotoCapaAnimal', 'Observacao']


class TpAnimal(ModelForm):
    class Meta:
        model = TipoAnimal
        fields = ['TipoAnimal']
    
class RcAnimal(ModelForm):
    class Meta:
        model = RacaAnimal
        fields = ['TipoAnimal', 'RacaAnimal']

class AdotAnimal(ModelForm):
    class Meta:
        model = RacaAnimal
        fields="__all__"

class AdmVoluntarios(ModelForm):
    class Meta:
        model = Voluntarios
        fields="__all__"    

class AdmCargo(ModelForm):
    class Meta:
        model = Cargo
        fields="__all__" 

class AdmFuncionarios(ModelForm):
    class Meta:
        model = Funcionarios
        fields="__all__"      

class AdmSobre(ModelForm):
    class Meta:
        model = Sobre
        #fields = ['content', 'added_time']
        fields = '__all__'

class AdmDoacao(ModelForm):
    class Meta:
        model = Doador
        #fields = ['content', 'added_time']
        fields = '__all__'

class AdmDuvidas(ModelForm):
    class Meta:
        model = Duvidas
        #fields = ['content', 'added_time']
        fields = '__all__'

class AdmUser(ModelForm):
    class Meta:
        model = User
        #fields = ['content', 'added_time']
        fields = '__all__'

class AdoteForm(ModelForm):
    class Meta:
        model = Adotante
        fields = ["NomeAdotante","TelefoneAdotante","EmailAdotante","CepAdotante","RuaAdotante", "NumCasaAdotante","BairroAdotante","CidadeAdotante","AnimalAdotante","ObsAdotante"
        ]