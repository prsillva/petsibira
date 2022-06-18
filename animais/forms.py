from django.forms import ModelForm
from blog.models import Animais

class AddAnimal(ModelForm):
    class Meta:
        model = Animais
        fields = ['NomeAnimal', 'IdadeAnimal', 'TipoAnimal', 'RacaAnimal', 'PesoAnimal','CorAnimal', 'Vacinado', 'Adotado', 'FotoCapaAnimal', 'Observacao']