from django.db import models

class Curso(models.Model):
    sigla_ies =	models.CharField(max_length=5)
    nome_ies =	models.CharField(max_length=20)
    categoria_administrativa = 	models.CharField(max_length=20)
    organização_academica =  models.CharField(max_length=20)
    situacao_ies =models.CharField(max_length=20)
    duracao =models.IntegerField()
    college_code = models.IntegerField()

class Faculdade(models.Model):
    nome_curso = models.CharField(max_length=25)
    area_curso = models.CharField(max_length=25)
    descricao_curso = models.TextField()
    salario_estag = models.IntegerField()
    salario_junior = models.IntegerField()
    salario_pleno = models.IntegerField()
    salario_senior = models.IntegerField()


class Curso_Faculdade(models.Model):
    codigo_curso = models.IntegerField(null=True)	
    Sigla_da_IES	= models.CharField(max_length=500)
    Nome_da_IES	= models.CharField(max_length=500)
    Categoria_Administrativa= models.CharField(max_length=500)	
    Organizacao_Academica	= models.CharField(max_length=500)

class Curso_teste(models.Model):
    codigo_curso = models.IntegerField()
    codigo_ies= models.IntegerField()
    sigla_ies=models.CharField(max_length=500)
    nome_ies =models.CharField(max_length=500)


############################################################
