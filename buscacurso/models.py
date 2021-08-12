from django.db import models

class Curso(models.Model):
    sigla_ies =	models.CharField(max_length=5)
    nome_ies =	models.CharField(max_length=20)
    categoria_administrativa = 	models.CharField(max_length=20)
    organização_academica =  models.CharField(max_length=20)
    situacao_ies =models.CharField(max_length=20)
    duracao =models.IntegerField()

