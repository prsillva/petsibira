from django.db import models


class Cargo(models.Model):
    Cargo = models.CharField(max_length=20, verbose_name='Cargo')
    def __str__(self):
        return self.Cargo
    class Meta:
            verbose_name_plural = "Cargos"

class Funcionarios(models.Model):
    Nome = models.CharField(max_length=80, verbose_name='Nome Completo')
    Cpf = models.CharField(max_length=20, verbose_name='CPF')
    Telefone = models.CharField(max_length=80, verbose_name='Telefone')
    Email = models.EmailField(max_length=50, verbose_name='E-mail')
    Cep = models.CharField(max_length=80, verbose_name='Cep')
    Rua = models.CharField(max_length=25, verbose_name='Rua')
    Bairro = models.CharField(max_length=80, verbose_name='Bairro')
    Cidade = models.CharField(max_length=30, verbose_name='Cidade')
    Estado = models.CharField(max_length=10, verbose_name='Estado')
    Cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, verbose_name='Cargo')
    def __str__(self):
        return self.Nome
    class Meta:
            verbose_name_plural = "Funcionários"