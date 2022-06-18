from django.forms import ModelForm
from home.models import Voluntarios
from django import forms
from doacao.models import Doador


class AddVoluntario(ModelForm):
    class Meta:
        model = Voluntarios
        fields = ['NomeVoluntario', 'TelefoneVoluntario', 'EmailVoluntario', 'IdadeVoluntario', 'TempoDisponivelHrsMes','CepVoluntario', 'RuaVoluntario', 'NumCasaVoluntario', 'BairroVoluntario', 'CidadeVoluntario','MensagemVoluntario']

class Voluntario(forms.Form):
       NomeVoluntario = forms.CharField()
       TelefoneVoluntario = forms.CharField()
       EmailVoluntario = forms.EmailField(label='E-mail')
       IdadeVoluntario = forms.CharField()
       TempoDisponivelHrsMes = forms.CharField()
       CepVoluntario = forms.CharField()
       RuaVoluntario = forms.CharField()
       NumCasaVoluntario = forms.CharField()
       BairroVoluntario = forms.CharField()
       CidadeVoluntario = forms.CharField()
       MensagemVoluntario = forms.CharField(widget=forms.Textarea())

class DoadorForm(ModelForm):
    class Meta:
        model = Doador
        fields=['NomeDoador', 'TelefoneDoador', 'EmailDoador', 'TipoDoacao', 'QtdDoacao', 'CepDoador', 'RuaDoador', 'NumeroCasaDoador','BairroDoador', 'CidadeDoador', 'EstadoDoador','Observacao', 'DeAcordoDoador']


