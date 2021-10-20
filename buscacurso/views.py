from django.shortcuts import get_object_or_404, render
#from .models import Curso, Curso_teste, Faculdade
from .models import *
import requests
from django.shortcuts import render

def index (request):
    return render(request, 'index.html')

#passo 2 criar função
##def course_list(request):
#    faculdades= Curso_teste.objects.all
#
 #   dados = {
  #      'faculdades' :faculdades
   # }

    return render(request, 'course_list.html',dados)
def course_list(request):
    #faculdades= Faculdade.objects.all
    courses_inst= CoursesInstitution.objects.all
    courses=Courses.objects.all
    institution=Institution.objects.all
    maintainer=Maintainer.objects.all

    dados = {
        #'faculdades' :faculdades
        'courses_inst' : courses_inst,
        'courses' : courses,
        'institution' : institution,
        'maintainer' : maintainer
    }

    return render(request, 'course_list.html',dados)

def details(request,faculdade_id):
    cursos = Curso.objects.all
    faculdades = Faculdade.objects.all
    curso_teste = Curso_teste.objects.all
    detalhes = get_object_or_404(Faculdade, pk = faculdade_id)

    faculdade_a_exibir ={
        'curso_teste':curso_teste,
        'faculdade' : detalhes,
        'cursos' :cursos,
        'faculdades': faculdades
    }



    return render(request, 'details.html',faculdade_a_exibir)

def support(request):
    return render(request, 'support.html')


