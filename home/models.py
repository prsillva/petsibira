from django.db import models

# Create your models here.
class Sobre(models.Model):
    titulo = models.CharField(max_length=30, verbose_name= 'Titulo da Pagina Sobre')
    imagem_sobre = models.ImageField(upload_to='media/', null=True, verbose_name='Imagem Sobre')
    texto_sobre = models.TextField(null=False, verbose_name='Texto Sobre do Site')
    status = models.BooleanField(default=False)

    def __str__(self):
            return str(self.titulo)
    
    class Meta:
            verbose_name_plural= "Sobre"

class Duvidas(models.Model):
    pergunta = models.CharField(max_length=50, verbose_name="Pergunta Dúvida")
    texto_pergunta = models.TextField(verbose_name="Resposta", default='')
    def __str__(self):
            return str(self.pergunta)
    
    class Meta:
            verbose_name_plural= "Dúvidas"

class Voluntarios(models.Model):

    NomeVoluntario = models.CharField(max_length=80, verbose_name='Nome Completo')
    TelefoneVoluntario = models.CharField(max_length=15, verbose_name='Telefone')
    EmailVoluntario =  models.CharField(max_length=80, verbose_name='E-mail')
    IdadeVoluntario =  models.CharField(max_length=2, verbose_name='Idade')
    TempoDisponivelHrsMes =  models.CharField(max_length=3, verbose_name='Horas por mês de voluntariado')
    CepVoluntario = models.CharField(max_length=15, verbose_name='Cep')
    RuaVoluntario = models.CharField(max_length=50, verbose_name='Rua/Logradouro')
    NumCasaVoluntario =  models.CharField(max_length=80, verbose_name='Número')
    BairroVoluntario =  models.CharField(max_length=80, verbose_name='Bairro')
    CidadeVoluntario =  models.CharField(max_length=80, verbose_name='Cidade')
    MensagemVoluntario = models.TextField(null=False, verbose_name='Observação')
    
    def __str__(self):
        return self.NomeVoluntario
    
    class Meta:
            verbose_name_plural = "Voluntários"
