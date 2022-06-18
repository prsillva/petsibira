from django.db import models


# Create your models here.
class Doador(models.Model):
    TipoDoacao = (
    ('Alimento', 'Alimento'),
    ('Medicamentos', 'Medicamentos')
    )
    NomeDoador = models.CharField(max_length=80, verbose_name='Nome Completo')
    TelefoneDoador = models.CharField(max_length=20, verbose_name='Telefone')
    EmailDoador = models.EmailField(max_length=80, verbose_name='E-mail')
    TipoDoacao = models.CharField(max_length=15, choices=TipoDoacao, verbose_name='Tipo de Doação')
    QtdDoacao = models.CharField(max_length=80, verbose_name='Qtd Doação')
    CepDoador = models.CharField(max_length=25, verbose_name='Cep')
    RuaDoador = models.CharField(max_length=80, verbose_name='Rua')
    NumeroCasaDoador =models.CharField(max_length=6, verbose_name='Número')
    BairroDoador = models.CharField(max_length=30, verbose_name='Bairro')
    CidadeDoador = models.CharField(max_length=80, verbose_name='Cidade')
    EstadoDoador = models.CharField(max_length=30, verbose_name='Estado')
    Observacao = models.TextField(null=False, verbose_name='Observação')
    DeAcordoDoador = models.BooleanField(default=False, verbose_name='Selecione para concordar')
    def __str__(self):
        return self.NomeDoador
    class Meta:
            verbose_name_plural = "Doadores"