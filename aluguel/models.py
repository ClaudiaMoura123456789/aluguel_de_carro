from django.db import models
from django.contrib.auth.models import User


class Carro(models.Model):
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    ano = models.IntegerField('Ano de Fabricação')
    disponivel = models.BooleanField(default=True)
    preco = models.PositiveSmallIntegerField('Preço') 
    foto = models.ImageField(upload_to='foto', null=True,blank=True)

    def __str__(self):
        return self.modelo

class Aluguel(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    data_inicial = models.DateField()
    data_final = models.DateField()
