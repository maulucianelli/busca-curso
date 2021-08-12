from django.shortcuts import render
from .models import Curso

def index (request):
    return render(request, 'index.html')

#passo 2 criar função

def course_list(request):
    return render(request, 'course_list.html')

def details(request):
    cursos = Curso.objects.all

    dados = {
        'cursos' :cursos
    }

    return render(request, 'details.html',dados)

def support(request):
    return render(request, 'support.html')
