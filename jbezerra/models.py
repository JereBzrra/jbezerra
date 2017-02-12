from django.db import models
from django.utils import timezone

class Slide(models.Model):
    imagem = models.CharField(max_length=6)

class Critica(models.Model):
    ano = models.IntegerField()
    fonte = models.CharField(max_length=100)
    critico = models.CharField(max_length=50)
    titulo = models.CharField(max_length=200)
    critica = models.TextField()
    exibe_critico = models.IntegerField()
    link_critico = models.CharField(max_length=50,default='')
    exibe_menu = models.IntegerField(default=0)

class Obra(models.Model):
    nome = models.CharField(max_length=100)
    tecnica = models.CharField(max_length=50)
    formato = models.CharField(max_length=20)
    ano = models.IntegerField()
    fase = models.IntegerField()
    colecao = models.BooleanField()
    ativo = models.BooleanField()
    slide = models.BooleanField()
    facebook = models.BooleanField()
