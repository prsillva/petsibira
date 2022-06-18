from django.forms import ModelForm
from .models import Adotante
 


class AdotarForm(ModelForm):
    class Meta:
        model = Adotante
        fields = ["NomeAdotante","TelefoneAdotante","EmailAdotante","CepAdotante","RuaAdotante", "NumCasaAdotante","BairroAdotante","CidadeAdotante","AnimalAdotante","ObsAdotante"
        ]