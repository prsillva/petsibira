from django.db import models

from blog.models import Animais

# Create your models here.
class Adotante(models.Model):

      NomeAdotante = models.CharField(max_length=80, verbose_name='Nome Completo')
      TelefoneAdotante = models.CharField(max_length=20, verbose_name='Telefone')
      EmailAdotante = models.EmailField(max_length=80, verbose_name='E-mail')
      CepAdotante = models.CharField(max_length=25, verbose_name='Cep')
      RuaAdotante = models.CharField(max_length=80, verbose_name='Rua')
      NumCasaAdotante = models.CharField(max_length=6, verbose_name='Número')
      BairroAdotante = models.CharField(max_length=30, verbose_name='Bairro')
      CidadeAdotante = models.CharField(max_length=80, verbose_name='Cidade')
      EstadoAdotante = models.CharField(max_length=80, verbose_name='Estado')
      AnimalAdotante = models.CharField(max_length=80, verbose_name='Animal escolhido')
      ObsAdotante = models.TextField(null=False, verbose_name='Observação')
def __str__(self):
    return self.NomeAdotante
class Meta:
        verbose_name_plural = "Adotantes"