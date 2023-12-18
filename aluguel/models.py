from django.db import models
from django.contrib.auth.models import User


class Carro(models.Model):
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)

class Aluguel(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_inicial = models.DateField()
    data_final = models.DateField()
