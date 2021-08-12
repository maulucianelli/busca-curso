from django.shortcuts import render
from .models import Curso, Faculdade

def index (request):
    return render(request, 'index.html')

#passo 2 criar função
def course_list(request):
    faculdades= Faculdade.objects.all

    dados = {
        'faculdades' :faculdades
    }

    return render(request, 'course_list.html',dados)

def details(request):
    cursos = Curso.objects.all
    faculdades = Faculdade.objects.all
    dados = {
        'cursos' :cursos,
        'faculdades': faculdades
    }

    return render(request, 'details.html',dados)

def support(request):
    return render(request, 'support.html')
