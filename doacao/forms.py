from django.forms import ModelForm
from .models import Doador
from django import forms


class DoadorForm(ModelForm):
    class Meta:
        model = Doador
        fields=['NomeDoador', 'TelefoneDoador', 'EmailDoador', 'TipoDoacao', 'QtdDoacao', 'CepDoador', 'RuaDoador', 'NumeroCasaDoador','BairroDoador', 'CidadeDoador', 'EstadoDoador','Observacao', 'DeAcordoDoador']