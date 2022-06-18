from django.db import models
from django.contrib.auth.models import User



class Post (models.Model):
    STATUS = (
    ('active', 'Ativo'),
    ('draft', 'Rascunho')
    )
    title = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField()
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    created_at = models.DateField(auto_now_add=True, verbose_name='criado em')
    updated_at = models.DateField(auto_now=True, verbose_name='atualizado em')
    status = models.CharField(max_length=15, choices=STATUS)

    def __str__(self):
     return self.title

class TipoAnimal(models.Model):
    TipoAnimal = models.CharField(max_length=20, verbose_name='Tipo de Animal')
    def __str__(self):
        return self.TipoAnimal
    class Meta:
            verbose_name_plural = "Tipos de Animais"

        
class RacaAnimal(models.Model):
    TipoAnimal = models.ForeignKey(TipoAnimal, on_delete=models.CASCADE, verbose_name='Tipo de Animal')
    RacaAnimal = models.CharField(max_length=30, verbose_name='Raça do Animal')
    def __str__(self):
        return self.RacaAnimal
    class Meta:
            verbose_name_plural = "Raças"

class Animais(models.Model):
    OPCAO = (
    ('Sim', 'Sim'),
    ('Não', 'Não')
    )
    Sexo = (
    ('Macho', 'Macho'),
    ('Femea', 'Femea')
    )
    NomeAnimal = models.CharField(max_length=80, verbose_name='Nome do Animal')
    IdadeAnimal = models.CharField(max_length=10, verbose_name='Idade aproxima do Animal')
    TipoAnimal = models.ForeignKey(TipoAnimal, on_delete=models.CASCADE, verbose_name='Tipo de Animal') 
    RacaAnimal = models.ForeignKey(RacaAnimal, on_delete=models.CASCADE, verbose_name='Raça do Animal') 
    PesoAnimal = models.CharField(max_length=5, verbose_name='Peso do Animal')
    CorAnimal = models.CharField(max_length=15, verbose_name='Cor do Animal')
    SexoAnimal = models.CharField(max_length=15, choices=Sexo, verbose_name='Sexo do Animal')
    Vacinado = models.CharField(max_length=15, choices=OPCAO, verbose_name='Vacinado?')
    Adotado = models.CharField(max_length=15, choices=OPCAO, verbose_name='Adotado?')
    FotoCapaAnimal = models.ImageField(upload_to='media/', null=True, verbose_name='Foto de Capa')
    Observacao = models.TextField(null=False, verbose_name='Observação')
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.NomeAnimal
    
    class Meta:
            verbose_name_plural = "Animais"

    
