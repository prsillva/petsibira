from django.db import models

# Create your models here.

class TipoDespesa(models.Model):
    TipoDespesa = models.CharField(max_length=20, verbose_name='Nome Despesa')
    def __str__(self):
        return self.TipoDespesa
    class Meta:
            verbose_name_plural = "Despesas"


class Despesas (models.Model):
    TipoDespesa = models.ForeignKey(TipoDespesa, on_delete=models.CASCADE, verbose_name='Tipo de Despesa')
    Descricao = models.TextField(verbose_name='Descrição')
    Valor = models.DecimalField(default = 0.00, max_digits=100, decimal_places = 2, verbose_name='Valor')
    criado_em = models.DateField(auto_now_add=True, verbose_name='Criado em')
    Quantidade = models.DecimalField(default = 0.00, max_digits=100, decimal_places = 2, verbose_name='Quantidade')
    Total= models.DecimalField(default = 0.00, max_digits=100, decimal_places = 2, verbose_name='Total')

    def __str__(self):
     return self.TipoDespesa