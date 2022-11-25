from distutils.command.upload import upload
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100 )
    valor = models.DecimalField('Preço do produto', max_digits=8,decimal_places=2)
    descricao = models.TextField(blank = True)
    img = models.ImageField(upload_to='media/', blank=True, null=True, max_length=250)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome